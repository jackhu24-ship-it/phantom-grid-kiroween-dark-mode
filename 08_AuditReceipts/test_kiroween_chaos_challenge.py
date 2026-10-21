"""
PHANToM Grid :: 1,000-Cycle Extreme Chaos Challenge
Torture-tests the Frankenstein Polyglot Kernel and ASIL-D State Machine
"""

import pytest
import time
import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02_核心代碼庫_SourceCode")))

from core.frankenstein_kernel import FrankensteinKernel
from core.state_machine import DeterministicStateMachine, FSMState
from core.zdr_scrubber import ZDRScrubber


def test_1000_chaos_cycles():
    kernel = FrankensteinKernel()
    fsm = DeterministicStateMachine(vram_ceiling_gb=50.0)
    scrubber = ZDRScrubber()

    total_runs = 1000
    passed_runs = 0

    t_start = time.perf_counter()

    for i in range(total_runs):
        # 1. Random vector generation
        dim = random.randint(16, 128)
        vec = [random.uniform(-100.0, 100.0) for _ in range(dim)]
        
        # 2. Rust RMSNorm execution
        norm_vec, lat_us = kernel.compute_rmsnorm_rust(vec)
        assert len(norm_vec) == dim

        # 3. Random condition number (some <= 10, some > 10 triggering 1.35x damping)
        sigma = random.uniform(0.1, 25.0)
        eval_res = kernel.evaluate_triton_sram_geometry(sigma)
        assert eval_res["effective_sigma"] is not None

        # 4. State transitions
        fsm.reset_to_standby()
        fsm.transition_to(FSMState.INGRESS)
        fsm.transition_to(FSMState.COMPUTING, context={"vram_requested_gb": random.uniform(10.0, 48.0)})
        fsm.transition_to(FSMState.AUDIT_GATE)
        fsm.transition_to(FSMState.CLEARED)
        fsm.transition_to(FSMState.DISPATCHED)

        # 5. ZDR memory wipe
        buf = bytearray(random.randint(64, 512))
        res = scrubber.scrub_buffer(buf)
        assert res["verified_zero"] is True

        passed_runs += 1

    total_elapsed = time.perf_counter() - t_start
    qps = total_runs / total_elapsed

    print(f"\n[CHAOS VERIFIER] {passed_runs}/{total_runs} iterations PASS in {total_elapsed:.3f}s ({qps:.1f} QPS)")
    assert passed_runs == total_runs
    assert scrubber.verify_zero_residual() == 0.000000
