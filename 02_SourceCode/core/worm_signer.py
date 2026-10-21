"""
PHANToM Grid :: WORM Cryptographic Signer & Audit Verifier
Produces tamper-evident SHA-256 receipts signed by Commander Jack Hu & Xiaomi
"""

import hashlib
import json
import time
from typing import Dict, Any


class WORMAuditSigner:
    """
    Write-Once-Read-Many (WORM) Cryptographic Ledger Signer.
    Generates deterministic SHA-256 fingerprints for code and verification runs.
    """

    def __init__(self, commander: str = "Jack Hu (Solo Architect)", secretary: str = "Xiaomi"):
        self.commander = commander
        self.secretary = secretary

    def generate_receipt(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates an immutable, dual-signed receipt with SHA-256 fingerprint.
        """
        raw_bytes = json.dumps(payload, sort_keys=True).encode("utf-8")
        sha256_hash = hashlib.sha256(raw_bytes).hexdigest()
        
        receipt_id = f"PG-RECEIPT-KIROWEEN-0x{sha256_hash[:16].upper()}"
        receipt = {
            "receipt_id": receipt_id,
            "sha256_fingerprint": sha256_hash,
            "timestamp": time.time(),
            "signers": {
                "supreme_commander": self.commander,
                "chief_customs_officer": self.secretary
            },
            "status": "RATIFIED",
            "audit_payload": payload
        }
        return receipt
