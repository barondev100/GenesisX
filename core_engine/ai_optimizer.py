import logging
from core_engine.ai_modifier import AIModifier

class AIOPTimizer:
    """Forces AI functions to be modified without mercy."""

    def __init__(self, file_path):
        """Initialize the AI Optimizer with the file path."""
        self.file_path = file_path
        self.modifier = AIModifier(file_path)

    def optimize_functions(self, function_reports):
        """Aggressively rewrites AI functions that are inefficient."""
        protected_functions = {"run", "__init__"}  # **Don't touch these**

        for func, details in function_reports.items():
            if func in protected_functions:
                continue  # **Don't modify protected functions**

            if details.get('contains_loops', False) and not details.get('contains_conditionals', False):
                logging.info(f"⚒️ REWRITING '{func}': Loop detected, must be optimized.")

                success = self.modifier.modify_function(func)  # **Force Rewrite**

                if success:
                    logging.info(f"✅ Function '{func}' has been successfully rewritten.")
                else:
                    logging.error(f"❌ Failed to modify '{func}'.")
