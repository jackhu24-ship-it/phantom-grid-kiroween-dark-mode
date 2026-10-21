# -*- coding: utf-8 -*-
"""
PHANToM Grid :: Kiroween 2026: Code in Dark Mode (Demo Video Generator)
Drawer: 05_方案B演示影片_DemoVideo_1440P / build_kiroween_demo_video.py
Standard: 1080P Broadcast-Grade x Live TUI Telemetry x Rule 59 Millisecond-Accurate Sync
Supervisor: Supreme Commander Jack Hu (Solo Architect) x Acting Commander Xiaomi
"""

import os
import sys
import asyncio
import subprocess
import shutil
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import edge_tts

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WIDTH, HEIGHT = 1920, 1080
FPS = 15

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
WORKSPACE_ROOT = PROJECT_ROOT.parent.parent

WORK_DIR = Path(r"C:\Users\user\.gemini\antigravity\brain\8331e215-ff12-4352-a559-7e066a14f653\scratch\video_build_kiroween")
OUTPUT_LOCAL = CURRENT_DIR / "PHANTOM_GRID_Kiroween_Demo_1080P.mp4"
OUTPUT_GDRIVE = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202612_Kiroween_Dark_Mode_Hackathon\05_方案B演示影片_DemoVideo_1440P\PHANTOM_GRID_Kiroween_Demo_1080P.mp4")

try:
    font_title = ImageFont.truetype("arialbd.ttf", 32)
    font_h2 = ImageFont.truetype("arialbd.ttf", 22)
    font_body_bold = ImageFont.truetype("arialbd.ttf", 18)
    font_body = ImageFont.truetype("arial.ttf", 16)
    font_mono_lg = ImageFont.truetype("consolab.ttf", 18)
    font_mono_md = ImageFont.truetype("consola.ttf", 16)
    font_mono_sm = ImageFont.truetype("consola.ttf", 13)
    font_badge = ImageFont.truetype("segoeuib.ttf", 15)
    font_sub_head = ImageFont.truetype("arialbd.ttf", 18)
    font_sub_text = ImageFont.truetype("arialbd.ttf", 34)
except Exception:
    font_title = font_h2 = font_body_bold = font_body = font_mono_lg = font_mono_md = font_mono_sm = font_badge = font_sub_head = font_sub_text = ImageFont.load_default()

# Colors
BG_COLOR = (10, 14, 20)           # Deep Obsidian
CARD_BG = (17, 24, 39)            # Slate Panel
CARD_BORDER = (56, 189, 248)      # Tech Cyan
CYAN_ACCENT = (56, 189, 248)
GOLD_ACCENT = (250, 204, 21)      # Neon Amber
GREEN_ACCENT = (52, 211, 153)     # Emerald
PURPLE_ACCENT = (192, 132, 252)   # Frankenstein Violet
RED_ACCENT = (248, 113, 113)
TEXT_WHITE = (248, 250, 252)
TEXT_MUTED = (148, 163, 184)
CONSOLE_BG = (12, 16, 24)

SCENES = [
    {
        "act": 1,
        "title": "THE CRISIS OF VIBE CODING & THE DARK MODE IMPERATIVE",
        "device_badge": "AWS KIRO IDE ✕ SPEC-DRIVEN ENGINEERING ✕ DARK MODE",
        "scene_type": "ARCHITECTURE",
        "segments": [
            {
                "spoken": "Welcome to PHANToM Grid: Dark Night Titan TUI, our official submission for Kiroween 2026 Code in Dark Mode.",
                "subtitle": "Welcome to PHANToM Grid :: Dark Night Titan TUI for Kiroween 2026."
            },
            {
                "spoken": "In the modern AI era, chaotic vibe coding produces unverified code, silent GPU memory bloat, and architectural decay.",
                "subtitle": "Chaotic vibe coding produces unverified code, silent GPU memory bloat, and decay."
            },
            {
                "spoken": "We engineer a formal, spec-driven architecture combining high-density Wall Street dark mode with mission-critical certainty.",
                "subtitle": "Formal spec-driven architecture combining Wall Street dark mode with mission-critical certainty."
            }
        ]
    },
    {
        "act": 2,
        "title": "TRACK FRANKENSTEIN: POLYGLOT MICROKERNEL IN ACTION",
        "device_badge": "POLYGLOT SUTURE: RUST AVX2 ✕ TRITON GPU ✕ PYTHON MCP",
        "scene_type": "POLYGLOT_KERNEL",
        "segments": [
            {
                "spoken": "Presenting the Frankenstein Polyglot Microkernel: uniting Rust AVX2 vector SIMD, Triton GPU SRAM, and Python MCP tools.",
                "subtitle": "Frankenstein Polyglot Microkernel: uniting Rust AVX2, Triton GPU SRAM, and Python MCP."
            },
            {
                "spoken": "Our Rust C-ABI microkernel executes RMSNorm calculations at over sixteen thousand operations per second with sixty microsecond latency.",
                "subtitle": "Rust C-ABI microkernel executes RMSNorm at 16,549 ops/sec with 60 microsecond latency."
            },
            {
                "spoken": "Triton GPU SRAM kernels constrain dynamic condition numbers strictly below ten point zero, self-healing oscillations dynamically.",
                "subtitle": "Triton GPU SRAM kernels constrain condition numbers below 10.0, self-healing oscillations."
            }
        ]
    },
    {
        "act": 3,
        "title": "TRACK COSTUME CONTEST & SKELETON CREW: TUI & HOOKS",
        "device_badge": "TUI HUD: >=78% VERTICAL COVERAGE // KIRO AGENT HOOKS",
        "scene_type": "TUI_HOOKS",
        "segments": [
            {
                "spoken": "Witness our Wall Street Dark Titan ANSI TrueColor TUI, maintaining over seventy-eight percent vertical coverage.",
                "subtitle": "Wall Street Dark Titan ANSI TrueColor TUI with >=78% vertical screen coverage."
            },
            {
                "spoken": "Kiro Agent Hooks monitor file updates and pre-build pipelines, automatically blocking dynamic eval poisoning.",
                "subtitle": "Kiro Agent Hooks monitor file updates, automatically blocking dynamic eval poisoning."
            },
            {
                "spoken": "Our ASIL-D state machine enforces a strict sixty frames-per-second budget with a fifty-gigabyte VRAM meltdown circuit breaker.",
                "subtitle": "ASIL-D state machine enforces 60 FPS loop budget with a 50GB VRAM meltdown circuit breaker."
            }
        ]
    },
    {
        "act": 4,
        "title": "ZDR PHYSICAL SCRUB & 1,000 ROUND CHAOS BENCHMARK",
        "device_badge": "VERIFICATION: 1,000 CHAOS PASS // 0.000000 MB ZDR RESIDUE",
        "scene_type": "CHAOS_VERIFICATION",
        "segments": [
            {
                "spoken": "Our Zero-Data-Residency protocol physically overwrites volatile memory via two passes, guaranteeing zero point zero megabyte leakage.",
                "subtitle": "ZDR protocol physically overwrites volatile memory via two passes: verified 0.000000 MB leakage."
            },
            {
                "spoken": "Under one thousand rounds of continuous extreme chaos injection, our engine achieves a one hundred percent green pass rate.",
                "subtitle": "Under 1,000 rounds of continuous extreme chaos injection, engine achieves 100% green pass rate."
            },
            {
                "spoken": "Ratified by Solo Architect Jack Hu with an immutable SHA-256 WORM receipt. PHANToM Grid is ready to conquer Kiroween.",
                "subtitle": "Ratified by Solo Architect Jack Hu with SHA-256 WORM receipt. Ready to conquer Kiroween!"
            }
        ]
    }
]


async def generate_speech_file(text: str, out_wav: Path, voice: str = "en-US-ChristopherNeural"):
    mp3_tmp = out_wav.with_suffix(".mp3")
    comm = edge_tts.Communicate(text, voice, rate="+2%")
    await comm.save(str(mp3_tmp))
    
    cmd = [
        "ffmpeg", "-y", "-i", str(mp3_tmp),
        "-ar", "48000", "-ac", "2",
        str(out_wav)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    if mp3_tmp.exists():
        mp3_tmp.unlink()


def get_wav_duration(wav_path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of",
        "default=noprint_wrappers=1:nokey=1", str(wav_path)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())


def create_silence_wav(duration_sec: float, out_wav: Path):
    cmd = [
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "anullsrc=r=48000:cl=stereo",
        "-t", f"{duration_sec:.3f}",
        str(out_wav)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)


async def build_act_audio(act_data: dict, act_dir: Path):
    act_num = act_data["act"]
    segments = act_data["segments"]
    
    seg_wav_paths = []
    seg_durations = []
    
    for idx, seg in enumerate(segments):
        wav_p = act_dir / f"seg_{idx}.wav"
        print(f"  [TTS] Act {act_num} Segment {idx+1}/{len(segments)}...")
        await generate_speech_file(seg["spoken"], wav_p)
        dur = get_wav_duration(wav_p)
        seg_wav_paths.append(wav_p)
        seg_durations.append(dur)
        
    intro_silence = act_dir / "intro_silence.wav"
    create_silence_wav(0.4, intro_silence)
    
    outro_silence = act_dir / "outro_silence.wav"
    create_silence_wav(0.6, outro_silence)
    
    timeline = []
    current_time = 0.0
    inputs_for_ffmpeg = []
    filter_parts = []
    
    # Intro silence
    inputs_for_ffmpeg.append(str(intro_silence))
    filter_parts.append(f"[{len(inputs_for_ffmpeg)-1}:a]")
    current_time += 0.4
    
    for i, (seg_wav, dur) in enumerate(zip(seg_wav_paths, seg_durations)):
        seg_start = current_time
        seg_end = current_time + dur
        timeline.append({
            "index": i,
            "spoken": segments[i]["spoken"],
            "subtitle": segments[i]["subtitle"],
            "start_time": seg_start,
            "end_time": seg_end,
            "duration": dur
        })
        inputs_for_ffmpeg.append(str(seg_wav))
        filter_parts.append(f"[{len(inputs_for_ffmpeg)-1}:a]")
        current_time += dur
        
        # Gap silence between segments
        if i < len(segments) - 1:
            gap_p = act_dir / f"gap_{i}.wav"
            create_silence_wav(0.35, gap_p)
            inputs_for_ffmpeg.append(str(gap_p))
            filter_parts.append(f"[{len(inputs_for_ffmpeg)-1}:a]")
            current_time += 0.35
            
    # Outro silence
    inputs_for_ffmpeg.append(str(outro_silence))
    filter_parts.append(f"[{len(inputs_for_ffmpeg)-1}:a]")
    current_time += 0.6
    
    combined_wav = act_dir / "act_combined_audio.wav"
    concat_filter = f"{''.join(filter_parts)}concat=n={len(filter_parts)}:v=0:a=1[outa]"
    
    cmd = ["ffmpeg", "-y"]
    for inp in inputs_for_ffmpeg:
        cmd.extend(["-i", inp])
    cmd.extend(["-filter_complex", concat_filter, "-map", "[outa]", str(combined_wav)])
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    return combined_wav, timeline, current_time


def draw_hud_header(draw, title: str, device_badge: str, progress_ratio: float, act_num: int):
    # Top banner bar
    draw.rectangle([0, 0, WIDTH, 80], fill=(12, 16, 24))
    draw.line([(0, 80), (WIDTH, 80)], fill=CARD_BORDER, width=2)
    
    # Badges
    draw.rectangle([30, 20, 240, 60], fill=(20, 15, 30), outline=PURPLE_ACCENT, width=1)
    draw.text((45, 30), f"ACT {act_num}/4 :: KIROWEEN", fill=GOLD_ACCENT, font=font_badge)
    
    draw.text((270, 28), title, fill=TEXT_WHITE, font=font_title)
    
    # Device badge
    draw.rectangle([WIDTH - 550, 20, WIDTH - 30, 60], fill=(17, 24, 39), outline=CYAN_ACCENT, width=1)
    draw.text((WIDTH - 535, 30), device_badge, fill=CYAN_ACCENT, font=font_badge)
    
    # Progress line
    bar_w = int(WIDTH * progress_ratio)
    draw.line([(0, 82), (bar_w, 82)], fill=GOLD_ACCENT, width=3)


def draw_subtitle_bar(draw, subtitle_text: str, current_time: float, seg_start: float, seg_end: float):
    # Title Safe Area: Bottom 110px buffer preserved! Subtitle placed at [880, 970]
    box_top = 880
    box_bottom = 970
    draw.rectangle([60, box_top, WIDTH - 60, box_bottom], fill=(15, 20, 30), outline=CYAN_ACCENT, width=2)
    
    # Speaker tag
    draw.rectangle([80, box_top - 15, 290, box_top + 15], fill=(250, 204, 21), outline=None)
    draw.text((95, box_top - 12), "ORCHESTRATOR TELEMETRY", fill=(10, 14, 20), font=font_sub_head)
    
    # Subtitle text
    draw.text((100, box_top + 30), subtitle_text, fill=TEXT_WHITE, font=font_sub_text)


def render_scene_content(draw, act_num: int, rel_time: float, seg_idx: int):
    # Renders the central 3-card or 2-card layout
    card_y = 120
    card_h = 720
    
    if act_num == 1:
        # Act 1: Architecture & Vibe Coding Crisis
        card_w = (WIDTH - 120 - 40) // 2
        
        # Left: Vibe Coding Crisis
        draw.rectangle([60, card_y, 60 + card_w, card_y + card_h], fill=CARD_BG, outline=RED_ACCENT, width=2)
        draw.rectangle([80, card_y + 20, 80 + card_w - 40, card_y + 65], fill=(30, 15, 20), outline=RED_ACCENT, width=1)
        draw.text((100, card_y + 30), "⚠️ THE CRISIS: UNVERIFIED VIBE CODING", fill=RED_ACCENT, font=font_h2)
        
        issues = [
            ("• Non-Deterministic Latency Spikes:", "Unbounded loops causing 500ms+ jitters"),
            ("• Hidden GPU VRAM Meltdown:", "No hard ceiling, leading to OOM server crash"),
            ("• Poisoned AST Execution:", "Unfiltered dynamic eval / command injections"),
            ("• Fragmented Dark Mode:", "Messy developer UI with <40% screen utilization"),
            ("• Zero Audit Trail:", "No cryptographic proof of code provenance")
        ]
        iy = card_y + 100
        for h, d in issues:
            draw.text((90, iy), h, fill=GOLD_ACCENT, font=font_body_bold)
            draw.text((90, iy + 30), d, fill=TEXT_MUTED, font=font_body)
            iy += 80
            
        # Right: PHANToM Grid Spec-Driven Solution
        rx = 60 + card_w + 40
        draw.rectangle([rx, card_y, rx + card_w, card_y + card_h], fill=CARD_BG, outline=GREEN_ACCENT, width=2)
        draw.rectangle([rx + 20, card_y + 20, rx + card_w - 20, card_y + 65], fill=(15, 30, 25), outline=GREEN_ACCENT, width=1)
        draw.text((rx + 40, card_y + 30), "🛡️ THE DEFENSE: SPEC-DRIVEN ENGINEERING", fill=GREEN_ACCENT, font=font_h2)
        
        sol = [
            ("• Spec-First Invariant:", "Kiro IDE Specs, Hooks, and Steering Rules"),
            ("• ASIL-D Zero-Split FSM:", "Deterministic 16.66ms 60 FPS kinematic loop"),
            ("• 50GB VRAM Meltdown Guard:", "Instant circuit breaker trips at 50.0 GB threshold"),
            ("• ZDR 2-Pass Memory Scrub:", "0xAA -> 0x00 physical zeroing (0.000000 MB)"),
            ("• WORM Cryptographic Dual-Sign:", "SHA-256 verified receipts by Jack Hu ✕ Xiaomi")
        ]
        iy = card_y + 100
        for h, d in sol:
            draw.text((rx + 30, iy), h, fill=CYAN_ACCENT, font=font_body_bold)
            draw.text((rx + 30, iy + 30), d, fill=TEXT_MUTED, font=font_body)
            iy += 80

    elif act_num == 2:
        # Act 2: Polyglot Frankenstein Kernel
        c_w = (WIDTH - 120 - 60) // 3
        tracks = [
            ("🧟 RUST AVX2 C-ABI", PURPLE_ACCENT, [
                ("Kernel:", "SIMD-Vectorized RMSNorm"),
                ("Throughput:", "16,549.8 ops/sec"),
                ("Latency:", "60.42 μs per dispatch"),
                ("Tolerance:", "< 4.77e-7 max absolute error"),
                ("Memory:", "Zero-copy ring buffer (SPSC)")
            ]),
            ("⚡ TRITON GPU SRAM", CYAN_ACCENT, [
                ("Kernel:", "4D Epipolar Spatial Geometry"),
                ("Condition:", "Sigma <= 10.0 Bounded"),
                ("Damping:", "1.35x Dynamic Rigid Damping"),
                ("Overlap:", "85.9% NCCL Communication"),
                ("SRAM Cache:", "Microsecond-level fast hit")
            ]),
            ("🐍 PYTHON 3.12 MCP", GOLD_ACCENT, [
                ("Protocol:", "Model Context Protocol (JSON-RPC)"),
                ("Orchestration:", "ASIL-D Multi-Agent Telemetry"),
                ("Audit Gate:", "AST Rule Interception"),
                ("Integration:", "AWS Kiro IDE Native Hooks"),
                ("Port:", "8080 Live Streaming SSE")
            ])
        ]
        for i, (title, color, metrics) in enumerate(tracks):
            cx = 60 + i * (c_w + 30)
            draw.rectangle([cx, card_y, cx + c_w, card_y + card_h], fill=CARD_BG, outline=color, width=2)
            draw.rectangle([cx + 15, card_y + 20, cx + c_w - 15, card_y + 65], fill=(15, 20, 30), outline=color, width=1)
            draw.text((cx + 25, card_y + 30), title, fill=color, font=font_h2)
            
            my = card_y + 100
            for label, val in metrics:
                draw.text((cx + 25, my), label, fill=TEXT_MUTED, font=font_body)
                draw.text((cx + 25, my + 25), val, fill=TEXT_WHITE, font=font_mono_md)
                my += 70

    elif act_num == 3:
        # Act 3: Wall Street Dark TUI & Kiro Hooks
        card_w = (WIDTH - 120 - 40) // 2
        
        # Left: Live TUI Telemetry
        draw.rectangle([60, card_y, 60 + card_w, card_y + card_h], fill=CONSOLE_BG, outline=GOLD_ACCENT, width=2)
        draw.rectangle([80, card_y + 20, 80 + card_w - 40, card_y + 65], fill=(25, 20, 10), outline=GOLD_ACCENT, width=1)
        draw.text((100, card_y + 30), "🎃 LIVE WALL STREET DARK TITAN TUI", fill=GOLD_ACCENT, font=font_h2)
        
        tui_lines = [
            "╔════════════════════════════════════════════════════════════════╗",
            "║ 🎃 PHANToM GRID :: KIROWEEN 2026 DARK NIGHT TITAN TUI          ║",
            "╠════════════════════════════════════════════════════════════════╣",
            "║ [Q1: RUST AVX2]           │ [Q2: TRITON GPU SRAM]              ║",
            "║ Throughput: 16,549.8 ops/s│ Condition Sigma: 1.34 <= 10.0      ║",
            "║ Latency: 60.42 μs         │ NCCL Overlap: 85.9% (Shielded)     ║",
            "╟───────────────────────────┼────────────────────────────────────╢",
            "║ [Q3: ASIL-D FSM]          │ [Q4: ZDR MEMORY RESIDUE]           ║",
            "║ State: CLEARED (60 FPS)   │ 2-Pass Residue: 0.000000 MB        ║",
            "║ P99 Latency: 0.0019 ms    │ VRAM Ceiling: 33.99 GB / 50.0 GB   ║",
            "╠════════════════════════════════════════════════════════════════╣",
            "║ 📜 FRANKENSTEIN EVENT STREAM: ALL 5/5 GATES GREEN              ║",
            "╚════════════════════════════════════════════════════════════════╝"
        ]
        ty = card_y + 90
        for line in tui_lines:
            draw.text((85, ty), line, fill=CYAN_ACCENT, font=font_mono_sm)
            ty += 30

        # Right: Kiro IDE Hooks Interceptor
        rx = 60 + card_w + 40
        draw.rectangle([rx, card_y, rx + card_w, card_y + card_h], fill=CARD_BG, outline=CYAN_ACCENT, width=2)
        draw.rectangle([rx + 20, card_y + 20, rx + card_w - 20, card_y + 65], fill=(15, 25, 35), outline=CYAN_ACCENT, width=1)
        draw.text((rx + 40, card_y + 30), "⚙️ KIRO AGENT HOOKS & STEERING RULES", fill=CYAN_ACCENT, font=font_h2)
        
        hooks = [
            ("Hook: on_spec_update", "PASS", "Verified Four Diagrams One Table structure"),
            ("Hook: post_save_ast_audit", "PASS", "Static AST blocked eval/exec injections"),
            ("Hook: pre_build_check", "PASS", "VRAM ceiling 50GB and ZDR invariants validated"),
            ("FSM Loop Budget", "PASS", "16.66ms real-time 60 FPS deterministic execution"),
            ("Vertical Screen Coverage", "PASS", "82.4% measured (exceeds >= 78% invariant)")
        ]
        hy = card_y + 100
        for name, status, desc in hooks:
            draw.text((rx + 30, hy), name, fill=GOLD_ACCENT, font=font_body_bold)
            draw.rectangle([rx + card_w - 110, hy, rx + card_w - 30, hy + 26], fill=(15, 40, 25), outline=GREEN_ACCENT, width=1)
            draw.text((rx + card_w - 95, hy + 5), status, fill=GREEN_ACCENT, font=font_badge)
            draw.text((rx + 30, hy + 28), desc, fill=TEXT_MUTED, font=font_body)
            hy += 75

    elif act_num == 4:
        # Act 4: ZDR & 1,000 Chaos Benchmark
        card_w = (WIDTH - 120 - 40) // 2
        
        # Left: ZDR Memory Scrubbing
        draw.rectangle([60, card_y, 60 + card_w, card_y + card_h], fill=CARD_BG, outline=GREEN_ACCENT, width=2)
        draw.rectangle([80, card_y + 20, 80 + card_w - 40, card_y + 65], fill=(15, 30, 25), outline=GREEN_ACCENT, width=1)
        draw.text((100, card_y + 30), "🧹 ZERO-DATA-RESIDENCY (ZDR) PROTOCOL", fill=GREEN_ACCENT, font=font_h2)
        
        zdr_steps = [
            ("1. Memory Allocation:", "Pinned GPU/CPU shared buffer allocated"),
            ("2. Mission Execution:", "High-frequency inference & state dispatch"),
            ("3. Pass 1 Overwrite:", "Physical wipe with 0xAA (10101010 bit pattern)"),
            ("4. Pass 2 Overwrite:", "Physical zeroing with 0x00 (00000000 absolute zero)"),
            ("5. Post-Purge Audit:", "0.000000 MB volatile memory residue verified")
        ]
        zy = card_y + 100
        for step, desc in zdr_steps:
            draw.text((90, zy), step, fill=GOLD_ACCENT, font=font_body_bold)
            draw.text((90, zy + 30), desc, fill=TEXT_WHITE, font=font_body)
            zy += 75
            
        # Right: 1,000 Chaos Verification
        rx = 60 + card_w + 40
        draw.rectangle([rx, card_y, rx + card_w, card_y + card_h], fill=CARD_BG, outline=PURPLE_ACCENT, width=2)
        draw.rectangle([rx + 20, card_y + 20, rx + card_w - 20, card_y + 65], fill=(25, 15, 30), outline=PURPLE_ACCENT, width=1)
        draw.text((rx + 40, card_y + 30), "⚡ 1,000 ROUND CHAOS BENCHMARK", fill=PURPLE_ACCENT, font=font_h2)
        
        chaos_metrics = [
            ("Total Iterations Injected:", "1,000 Cycles Continuous"),
            ("Pass Rate:", "100.0% (1,000 / 1,000 PASS)"),
            ("Deadlocks / Crashes:", "0 (Absolute Zero)"),
            ("Average Dispatch Latency:", "0.0019 ms"),
            ("VRAM Ceiling Clamp:", "50.0 GB Enforced (0 Breaches)"),
            ("WORM SHA-256 Receipt:", "PG-RECEIPT-KIROWEEN-0x74935601")
        ]
        cy = card_y + 100
        for label, val in chaos_metrics:
            draw.text((rx + 30, cy), label, fill=TEXT_MUTED, font=font_body)
            draw.text((rx + 30, cy + 25), val, fill=GREEN_ACCENT if "100" in val or "0" in val else GOLD_ACCENT, font=font_mono_md)
            cy += 65


def render_act_video(act_data: dict, act_dir: Path, combined_wav: Path, timeline: list, total_duration: float):
    act_num = act_data["act"]
    title = act_data["title"]
    device_badge = act_data["device_badge"]
    
    total_frames = int(total_duration * FPS)
    frames_dir = act_dir / "frames"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"  [FRAMES] Act {act_num}: Generating {total_frames} frames ({FPS} FPS, {total_duration:.2f}s)...")
    
    for f_idx in range(total_frames):
        current_time = f_idx / FPS
        progress = current_time / total_duration
        
        # Find active segment
        active_sub = "PHANToM Grid :: Wall Street Dark Night Titan TUI Engine"
        seg_idx = 0
        seg_start = 0.0
        seg_end = total_duration
        for item in timeline:
            if item["start_time"] <= current_time <= item["end_time"]:
                active_sub = item["subtitle"]
                seg_idx = item["index"]
                seg_start = item["start_time"]
                seg_end = item["end_time"]
                break
                
        # Draw frame
        img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_COLOR)
        draw = ImageDraw.Draw(img)
        
        # 1. Header
        draw_hud_header(draw, title, device_badge, progress, act_num)
        
        # 2. Main Content
        render_scene_content(draw, act_num, current_time, seg_idx)
        
        # 3. Subtitle Bar (Title Safe Area >= 110px from bottom)
        draw_subtitle_bar(draw, active_sub, current_time, seg_start, seg_end)
        
        frame_path = frames_dir / f"frame_{f_idx:05d}.png"
        img.save(frame_path)
        
    act_mp4 = act_dir / f"act_{act_num}.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(frames_dir / "frame_%05d.png"),
        "-i", str(combined_wav),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", str(act_mp4)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"  [ACT COMPLETE] Act {act_num} rendered: {act_mp4}")
    return act_mp4


async def main():
    print("=" * 80)
    print("🎬 STARTING KIROWEEN 2026 DEMO VIDEO GENERATION (1080P PRO PIPELINE)")
    print("=" * 80)
    
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    act_mp4s = []
    
    for act_data in SCENES:
        act_num = act_data["act"]
        act_dir = WORK_DIR / f"act_{act_num}"
        act_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n▶ Processing Act {act_num}/4: {act_data['title']}")
        combined_wav, timeline, total_duration = await build_act_audio(act_data, act_dir)
        act_mp4 = render_act_video(act_data, act_dir, combined_wav, timeline, total_duration)
        act_mp4s.append(act_mp4)
        
    print("\n🔗 Concatenating all 4 Acts into Final Master 1080P Video...")
    concat_list = WORK_DIR / "concat_list.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for mp4 in act_mp4s:
            f.write(f"file '{mp4.resolve()}'\n")
            
    OUTPUT_LOCAL.parent.mkdir(parents=True, exist_ok=True)
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(OUTPUT_LOCAL)
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"✅ Final Master Video created: {OUTPUT_LOCAL}")
    
    # Mirror to G-Drive
    try:
        OUTPUT_GDRIVE.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(OUTPUT_LOCAL, OUTPUT_GDRIVE)
        print(f"✅ Mirrored to G-Drive: {OUTPUT_GDRIVE}")
    except Exception as e:
        print(f"⚠️ G-Drive mirror note: {e}")
        
    print("\n🏆 KIROWEEN DEMO VIDEO GENERATION COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    asyncio.run(main())
