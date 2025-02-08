import inspect
import logging

class AIReflector:
    """Handles AI self-reflection using the inspect module and dynamic execution."""

    def __init__(self, target_object):
        """Initialize with the AI instance or module."""
        self.target_object = target_object

    def get_function_info(self, function_name):
        """Retrieves metadata about a given function in the AI."""
        try:
            func = getattr(self.target_object, function_name, None)
            if not func or not inspect.isfunction(func):
                logging.error(f"❌ Function '{function_name}' not found.")
                return None

            func_info = {
                "name": function_name,
                "args": list(inspect.signature(func).parameters.keys()),
                "docstring": inspect.getdoc(func),
                "source": inspect.getsource(func)
            }
            logging.info(f"🔍 Retrieved function info: {func_info}")
            return func_info

        except Exception as e:
            logging.error(f"❌ Error retrieving function info: {e}")
            return None

    def execute_code(self, code_string, local_vars=None):
        """Executes a dynamically generated code snippet safely."""
        try:
            exec(code_string, {}, local_vars if local_vars else {})
            logging.info("✅ Executed code successfully.")
            return True
        except Exception as e:
            logging.error(f"❌ Execution failed: {e}")
            return False
