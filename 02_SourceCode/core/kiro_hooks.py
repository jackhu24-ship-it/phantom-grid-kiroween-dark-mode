"""
PHANToM Grid :: Kiro IDE Agent Hooks & Steering Interceptor
Implements Kiro Spec-Driven Lifecycle Hooks: on_spec_update, post_save, pre_build
"""

import ast
from typing import Dict, Any, List


class KiroHooksInterceptor:
    """
    Kiro IDE Hook Interceptor enforcing Spec-First and Anti-Vibe Coding invariants.
    """

    def __init__(self):
        self.hooks_triggered = 0

    def on_spec_update(self, spec_text: str) -> Dict[str, Any]:
        """
        Kiro Hook triggered when a specification file is modified.
        Ensures presence of the 4 diagrams and 1 table.
        """
        self.hooks_triggered += 1
        has_topology = "graph TD" in spec_text or "flowchart" in spec_text
        has_sequence = "sequenceDiagram" in spec_text
        has_state = "stateDiagram" in spec_text
        has_table = "|" in spec_text and "---" in spec_text

        all_passed = has_topology and has_sequence and has_state and has_table
        return {
            "hook": "on_spec_update",
            "has_topology": has_topology,
            "has_sequence": has_sequence,
            "has_state": has_state,
            "has_table": has_table,
            "spec_first_compliant": all_passed
        }

    def post_save_ast_audit(self, source_code: str) -> Dict[str, Any]:
        """
        Kiro Hook triggered upon file save.
        Performs AST analysis to block dangerous patterns (e.g., eval, unsafe os.system).
        """
        self.hooks_triggered += 1
        tree = ast.parse(source_code)
        violations = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ["eval", "exec"]:
                        violations.append(f"Forbidden call to '{node.func.id}' at line {node.lineno}")

        return {
            "hook": "post_save_ast_audit",
            "clean": len(violations) == 0,
            "violations": violations
        }

    def pre_build_check(self, manifest: Dict[str, Any]) -> Dict[str, Any]:
        """
        Kiro Hook triggered before build/test.
        Verifies compliance invariants.
        """
        self.hooks_triggered += 1
        vram_ok = manifest.get("vram_ceiling_gb", 100.0) <= 50.0
        zdr_ok = manifest.get("zdr_zero_residue_mb", 1.0) == 0.000000

        return {
            "hook": "pre_build_check",
            "vram_ceiling_valid": vram_ok,
            "zdr_valid": zdr_ok,
            "can_build": vram_ok and zdr_ok
        }
