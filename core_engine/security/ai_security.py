import ast
import logging

class AISecurity:
    """Enforces security layers to prevent AI from making unauthorized modifications."""

    PROTECTED_FUNCTIONS = {"run", "__init__", "monitor_execution"}
    UNSAFE_FUNCTION_CALLS = {"exec", "eval", "compile", "open", "__import__"}

    def __init__(self):
        logging.info("🔒 AI Security Module Initialized.")

    def enforce_security_policies(self, modified_code):
        """Checks if the AI modification violates security policies."""
        try:
            tree = ast.parse(modified_code)

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name in self.PROTECTED_FUNCTIONS:
                    logging.error(f"❌ Security Violation: Attempt to modify protected function '{node.name}'.")
                    return False

                if isinstance(node, ast.Call) and hasattr(node.func, "id") and node.func.id in self.UNSAFE_FUNCTION_CALLS:
                    logging.error(f"❌ Security Violation: Detected use of unsafe function '{node.func.id}' in modification.")
                    return False

            logging.info("✅ Security check passed. No unauthorized modifications detected.")
            return True
        except Exception as e:
            logging.error(f"❌ Security validation failed: {e}")
            return False
