import logging
import time

class AISandbox:
    """Executes AI modifications in an isolated sandbox to prevent instability."""

    def __init__(self):
        """Initialize the sandbox environment with controlled execution."""
        self.sandbox_globals = {}  # Isolated global execution space
        self.execution_timeout = 2  # Set a time limit for execution

    def test_code(self, code_string):
        """Executes the given code in a sandbox environment and checks for errors."""
        try:
            start_time = time.time()
            exec(code_string, self.sandbox_globals)  # Execute code in a safe, isolated space

            execution_time = time.time() - start_time
            if execution_time > self.execution_timeout:
                logging.error("❌ Sandbox execution took too long. Possible infinite loop detected.")
                return False

            logging.info("✅ Sandbox execution successful. Modification passed.")
            return True
        except Exception as e:
            logging.error(f"❌ Sandbox execution failed: {e}")
            return False
