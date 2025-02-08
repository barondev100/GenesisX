import ast
import logging
from core_engine.modification.ai_modifier import AIModifier

class AIFPL:
    """Implements Fractal Propagation Learning (FPL) for AI self-expansion."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.modifier = AIModifier(file_path)

    def analyze_and_expand(self):
        """Analyzes AI's functions and applies fractal expansion logic."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            source_code = file.read()
        
        tree = ast.parse(source_code)
        function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        
        logging.info(f"🔍 Identified {len(function_names)} functions for recursive expansion.")

        for function_name in function_names:
            if function_name not in {"__init__", "run"}:  # Avoid modifying critical methods
                self.expand_function(function_name)

    def expand_function(self, function_name):
        """Applies recursive modifications to a function, ensuring correct indentation."""
        
        # **Ensure proper indentation for new function expansion code**
        fractal_code = (
            f"    print('🔄 Expanding function: {function_name}')\n"
            f"    return {function_name}()\n"
        )

        logging.info(f"🔄 Applying fractal learning expansion to '{function_name}'.")
        success = self.modifier.modify_function(function_name, fractal_code)

        if success:
            logging.info(f"✅ Successfully expanded '{function_name}'.")
        else:
            logging.error(f"❌ Expansion failed for '{function_name}'.")
