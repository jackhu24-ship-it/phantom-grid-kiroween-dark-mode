"""
PHANToM Grid :: PitchDeck PDF Audit Verification
Checks that Kiroween_PitchDeck.pdf exists, has exactly 10 pages, and valid landscape geometry
"""

import os
import pypdf


def test_pitch_deck_pages_and_dimensions():
    pdf_path = os.path.join(os.path.dirname(__file__), "Kiroween_PitchDeck.pdf")
    assert os.path.exists(pdf_path), "PitchDeck PDF must exist!"

    reader = pypdf.PdfReader(pdf_path)
    assert len(reader.pages) == 10, f"PitchDeck must have exactly 10 pages, got {len(reader.pages)}"

    for i, page in enumerate(reader.pages):
        # Landscape check: width > height
        w = float(page.mediabox.width)
        h = float(page.mediabox.height)
        assert w > h, f"Page {i+1} must be landscape (w={w}, h={h})"
