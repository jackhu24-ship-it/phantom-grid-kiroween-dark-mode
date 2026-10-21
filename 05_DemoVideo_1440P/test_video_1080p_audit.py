"""
PHANToM Grid :: Demo Video 1080P Broadcast Audit
Verifies that PHANTOM_GRID_Kiroween_Demo_1080P.mp4 complies with Rule 59/60 standards
"""

import os
import subprocess
import json
import pytest


def get_video_metadata(video_path: str):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size:stream=width,height,codec_name,sample_rate",
        "-of", "json",
        video_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return json.loads(res.stdout)


def test_video_exists_and_size():
    video_path = os.path.join(os.path.dirname(__file__), "PHANTOM_GRID_Kiroween_Demo_1080P.mp4")
    assert os.path.exists(video_path), "Demo video MP4 must exist!"
    size_mb = os.path.getsize(video_path) / (1024 * 1024)
    assert size_mb >= 1.0, f"Video size should be >= 1MB, got {size_mb:.2f}MB"


def test_video_resolution_1080p():
    video_path = os.path.join(os.path.dirname(__file__), "PHANTOM_GRID_Kiroween_Demo_1080P.mp4")
    meta = get_video_metadata(video_path)
    video_stream = next(s for s in meta["streams"] if "width" in s)
    assert video_stream["width"] == 1920, f"Expected width 1920, got {video_stream['width']}"
    assert video_stream["height"] == 1080, f"Expected height 1080, got {video_stream['height']}"


def test_video_duration_window():
    video_path = os.path.join(os.path.dirname(__file__), "PHANTOM_GRID_Kiroween_Demo_1080P.mp4")
    meta = get_video_metadata(video_path)
    dur = float(meta["format"]["duration"])
    assert 100.0 <= dur <= 140.0, f"Video duration must be between 100s and 140s, got {dur:.2f}s"


def test_video_audio_stream():
    video_path = os.path.join(os.path.dirname(__file__), "PHANTOM_GRID_Kiroween_Demo_1080P.mp4")
    meta = get_video_metadata(video_path)
    audio_stream = next((s for s in meta["streams"] if s.get("codec_name") == "aac"), None)
    assert audio_stream is not None, "Video must contain an AAC audio stream"
