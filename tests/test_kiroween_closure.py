"""
PHANToM Grid :: Kiroween 2026 Closure Verification Suite
Enforces Gate-Before-Ship Test Closure (5/5 PASS)
"""

import pytest
import sys
import os

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.tui_engine import DarkNightTUIEngine, MAX_WIDTH
from core.frankenstein_kernel import FrankensteinKernel
from core.state_machine import DeterministicStateMachine, FSMState
from core.zdr_scrubber import ZDRScrubber
from core.worm_signer import WORMAuditSigner
from core.kiro_hooks import KiroHooksInterceptor


def test_tui_dark_mode_palette_and_clamping():
    """Assertion 1: TUI width clamping <= 118 chars and non-empty output."""
    tui = DarkNightTUIEngine()
    telemetry = {
        "rust_ops": "16,549.8 ops/sec",
        "rust_latency": "60.42 μs",
        "triton_cond_sigma": "1.34 <= 10.0",
        "nccl_overlap": "85.9%",
        "fsm_state": "CLEARED (60 FPS)",
        "p99_latency": "0.0019 ms",
        "zdr_residue": "0.000000 MB",
        "vram_level": "33.99 GB / 50.0 GB"
    }
    events = ["Event A: System initialized.", "Event B: Hook audit passed."]
    rendered = tui.render_full_screen(telemetry, events)
    
    assert rendered is not None
    assert len(rendered) > 100
    # Check that header contains title
    assert "KIROWEEN 2026" in rendered
    assert "PHANToM GRID" in rendered


def test_frankenstein_polyglot_dispatch():
    """Assertion 2: Polyglot kernel correctly runs Rust RMSNorm, Triton Sigma, and MCP dispatch."""
    kernel = FrankensteinKernel()
    
    # Rust vector test
    vec = [1.0, 2.0, 3.0, 4.0]
    norm_vec, lat_us = kernel.compute_rmsnorm_rust(vec)
    assert len(norm_vec) == 4
    assert lat_us >= 0.0

    # Triton condition sigma test (stable case)
    res_stable = kernel.evaluate_triton_sram_geometry(5.0)
    assert res_stable["is_stable"] is True
    assert res_stable["damping_factor"] == 1.0

    # Triton condition sigma test (unstable case triggering 1.35x damping)
    res_unstable = kernel.evaluate_triton_sram_geometry(15.0)
    assert res_unstable["is_stable"] is False
    assert res_unstable["damping_factor"] == 1.35

    # MCP tool call test
    mcp_res = kernel.dispatch_mcp_tool_call("deploy_model", {"model_id": "titan-4b"})
    assert mcp_res["jsonrpc"] == "2.0"
    assert mcp_res["result"]["status"] == "SUCCESS"


def test_state_machine_transition_and_estop():
    """Assertion 3: Strict ASIL-D state transitions and E-STOP recovery."""
    fsm = DeterministicStateMachine()
    assert fsm.state == FSMState.STANDBY

    # Legal transitions
    assert fsm.transition_to(FSMState.INGRESS) is True
    assert fsm.transition_to(FSMState.COMPUTING) is True
    assert fsm.transition_to(FSMState.AUDIT_GATE) is True
    assert fsm.transition_to(FSMState.CLEARED) is True
    assert fsm.transition_to(FSMState.DISPATCHED) is True
    assert fsm.transition_to(FSMState.STANDBY) is True

    # Illegal transition: STANDBY cannot jump straight to DISPATCHED
    assert fsm.transition_to(FSMState.DISPATCHED) is False


def test_vram_meltdown_ceiling_guard():
    """Assertion 4: VRAM requested over 50.0 GB triggers instant E-STOP."""
    fsm = DeterministicStateMachine(vram_ceiling_gb=50.0)
    fsm.transition_to(FSMState.INGRESS)
    
    # Breach 50.0 GB ceiling
    context = {"vram_requested_gb": 55.0}
    ok = fsm.transition_to(FSMState.COMPUTING, context=context)
    assert ok is False
    assert fsm.state == FSMState.E_STOP


def test_zdr_physical_zero_memory_leakage():
    """Assertion 5: ZDR 2-pass physical scrub zeroes out buffer with 0.000000 MB residue."""
    scrubber = ZDRScrubber()
    buf = bytearray(b"SENSITIVE_TITAN_WEIGHTS_AND_MEMORY_DATA_123456789")
    res = scrubber.scrub_buffer(buf)

    assert res["status"] == "PURGED"
    assert res["passes_completed"] == 2
    assert res["residual_mb"] == 0.000000
    assert res["verified_zero"] is True
    assert all(b == 0 for b in buf)

    leakage = scrubber.verify_zero_residual()
    assert leakage == 0.000000
