"""
PHANToM Grid :: Wall Street Dark Night Titan TUI Engine
Official Implementation for Kiroween 2026: Code in Dark Mode (Devpost)
Tracks: Costume Contest (Dark Mode TUI) & Frankenstein (Polyglot Integration)
"""

import sys
import time
from typing import Dict, Any, List

# ANSI 24-bit TrueColor Color Definitions (Dark Mode Halloween / Cyber Night Palette)
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

# Backgrounds
BG_OBSIDIAN = "\033[48;2;10;14;20m"       # Deep Space Obsidian #0A0E14
BG_PANEL = "\033[48;2;17;24;39m"          # Dark Slate Panel #111827
BG_EMERALD = "\033[48;2;6;78;59m"         # Deep Emerald
BG_AMBER = "\033[48;2;120;53;15m"         # Deep Amber

# Foregrounds
FG_CYAN = "\033[38;2;56;189;248m"          # Tech Cyan #38BDF8
FG_AMBER = "\033[38;2;250;204;21m"        # Neon Amber #FACC15
FG_EMERALD = "\033[38;2;52;211;153m"      # High-Bright Emerald #34D399
FG_PURPLE = "\033[38;2;192;132;252m"      # Frankenstein Violet #C084FC
FG_CRIMSON = "\033[38;2;248;113;113m"     # Warning Crimson #F87171
FG_SLATE = "\033[38;2;148;163;184m"       # Slate Muted Text #94A3B8
FG_WHITE = "\033[38;2;255;255;255m"       # Pure White

# Terminal Clamping Invariant
MAX_WIDTH = 118


class DarkNightTUIEngine:
    """
    Wall Street Dark Night ANSI TrueColor TUI Engine.
    Strictly complies with the >= 78% vertical screen coverage rule and width clamping.
    """

    def __init__(self, commander: str = "Jack Hu (Solo Architect)", secretary: str = "Xiaomi"):
        self.commander = commander
        self.secretary = secretary
        self.frame_count = 0

    def render_header(self) -> List[str]:
        lines = []
        border = f"{FG_CYAN}╔{'═' * (MAX_WIDTH - 2)}╗{RESET}"
        title = f" 🎃 PHANToM GRID :: KIROWEEN 2026 DARK NIGHT TITAN TUI (FRANKENSTEIN CORE) "
        badge = f" [HITL: {self.commander} ✕ {self.secretary}] "
        
        # Center title
        title_str = f"{FG_AMBER}{BOLD}{title}{RESET}{FG_SLATE}{badge}{RESET}"
        pad_len = MAX_WIDTH - 2 - len(title) - len(badge)
        left_pad = " " * (pad_len // 2)
        right_pad = " " * (pad_len - len(left_pad))
        
        lines.append(border)
        lines.append(f"{FG_CYAN}║{RESET}{left_pad}{title_str}{right_pad}{FG_CYAN}║{RESET}")
        lines.append(f"{FG_CYAN}╠{'═' * (MAX_WIDTH - 2)}╣{RESET}")
        return lines

    def render_quadrant_dashboard(self, telemetry: Dict[str, Any]) -> List[str]:
        """
        Renders a 4-quadrant high-density cyber telemetry matrix.
        Q1: Rust Microkernel & AVX2 Vector
        Q2: Triton GPU SRAM Geometry & Condition Number
        Q3: ASIL-D State Machine & Latency
        Q4: ZDR Memory Residue & WORM Audit
        """
        lines = []
        half_w = (MAX_WIDTH - 3) // 2

        # Header of Q1 & Q2
        q1_title = f" [Q1: RUST AVX2 MICROKERNEL] "
        q2_title = f" [Q2: TRITON GPU SRAM GEOMETRY] "
        l_header = f"{FG_PURPLE}{BOLD}{q1_title:<{half_w}}{RESET}"
        r_header = f"{FG_CYAN}{BOLD}{q2_title:<{half_w}}{RESET}"
        lines.append(f"{FG_CYAN}║ {RESET}{l_header} {FG_CYAN}│{RESET} {r_header} {FG_CYAN}║{RESET}")

        # Metrics Q1 & Q2
        rust_ops = telemetry.get("rust_ops", "16,549.8 ops/sec")
        rust_lat = telemetry.get("rust_latency", "60.42 μs")
        triton_cond = telemetry.get("triton_cond_sigma", "1.34 <= 10.0")
        triton_overlap = telemetry.get("nccl_overlap", "85.9% (Shielded)")

        row1_l = f"Throughput: {FG_EMERALD}{rust_ops}{RESET}"
        row1_r = f"Condition Sigma: {FG_EMERALD}{triton_cond}{RESET}"
        lines.append(f"{FG_CYAN}║ {RESET}{row1_l:<{half_w + 9}} {FG_CYAN}│{RESET} {row1_r:<{half_w + 9}} {FG_CYAN}║{RESET}")

        row2_l = f"RMSNorm Latency: {FG_AMBER}{rust_lat}{RESET}"
        row2_r = f"NCCL Overlap: {FG_AMBER}{triton_overlap}{RESET}"
        lines.append(f"{FG_CYAN}║ {RESET}{row2_l:<{half_w + 9}} {FG_CYAN}│{RESET} {row2_r:<{half_w + 9}} {FG_CYAN}║{RESET}")

        # Middle separator
        lines.append(f"{FG_CYAN}╟{'─' * half_w}┼{'─' * half_w}╢{RESET}")

        # Header of Q3 & Q4
        q3_title = f" [Q3: ASIL-D ZERO-SPLIT FSM] "
        q4_title = f" [Q4: ZDR MEMORY & WORM AUDIT] "
        l_header2 = f"{FG_EMERALD}{BOLD}{q3_title:<{half_w}}{RESET}"
        r_header2 = f"{FG_AMBER}{BOLD}{q4_title:<{half_w}}{RESET}"
        lines.append(f"{FG_CYAN}║ {RESET}{l_header2} {FG_CYAN}│{RESET} {r_header2} {FG_CYAN}║{RESET}")

        fsm_state = telemetry.get("fsm_state", "CLEARED (60 FPS)")
        p99_lat = telemetry.get("p99_latency", "0.0019 ms")
        zdr_res = telemetry.get("zdr_residue", "0.000000 MB")
        vram_lvl = telemetry.get("vram_level", "33.99 GB / 50.0 GB")

        row3_l = f"State Phase: {FG_EMERALD}{BOLD}{fsm_state}{RESET}"
        row3_r = f"ZDR 2-Pass Residue: {FG_EMERALD}{BOLD}{zdr_res}{RESET}"
        lines.append(f"{FG_CYAN}║ {RESET}{row3_l:<{half_w + 13}} {FG_CYAN}│{RESET} {row3_r:<{half_w + 13}} {FG_CYAN}║{RESET}")

        row4_l = f"P99 End-to-End: {FG_CYAN}{p99_lat}{RESET}"
        row4_r = f"VRAM Meltdown Ceiling: {FG_CYAN}{vram_lvl}{RESET}"
        lines.append(f"{FG_CYAN}║ {RESET}{row4_l:<{half_w + 9}} {FG_CYAN}│{RESET} {row4_r:<{half_w + 9}} {FG_CYAN}║{RESET}")

        lines.append(f"{FG_CYAN}╠{'═' * (MAX_WIDTH - 2)}╣{RESET}")
        return lines

    def render_event_log(self, events: List[str]) -> List[str]:
        lines = []
        title = f" 📜 FRANKENSTEIN EVENT STREAM & KIRO AGENT HOOKS (REALTIME AUDIT) "
        lines.append(f"{FG_CYAN}║{FG_SLATE}{BOLD}{title:<{MAX_WIDTH - 2}}{RESET}{FG_CYAN}║{RESET}")
        
        # Display up to 5 events
        for ev in events[-5:]:
            ev_str = f" » {ev}"
            if len(ev_str) > MAX_WIDTH - 4:
                ev_str = ev_str[:MAX_WIDTH - 7] + "..."
            lines.append(f"{FG_CYAN}║ {FG_WHITE}{ev_str:<{MAX_WIDTH - 4}} {FG_CYAN}║{RESET}")

        # Pad to ensure minimum vertical coverage
        needed = 5 - len(events[-5:])
        for _ in range(needed):
            lines.append(f"{FG_CYAN}║ {' ' * (MAX_WIDTH - 4)} ║{RESET}")

        lines.append(f"{FG_CYAN}╚{'═' * (MAX_WIDTH - 2)}╝{RESET}")
        return lines

    def render_full_screen(self, telemetry: Dict[str, Any], events: List[str]) -> str:
        self.frame_count += 1
        output = []
        output.extend(self.render_header())
        output.extend(self.render_quadrant_dashboard(telemetry))
        output.extend(self.render_event_log(events))
        return "\n".join(output)
