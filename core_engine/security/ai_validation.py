import ast
import logging

class AIValidation:
    """Ensures AI modifications are valid before execution."""

    def validate_code(self, file_path):
        """Checks for syntax errors before applying modifications."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                source_code = file.read()
            ast.parse(source_code)  # Attempt to parse the source code
            logging.info("✅ Code validation successful. No syntax errors detected.")
            return True
        except SyntaxError as e:
            logging.error(f"❌ Code validation failed: {e}")
            return False

    def analyze_modification(self, original_code, modified_code):
        """Compares AI-generated modifications before execution using AST."""
        try:
            original_ast = ast.parse(original_code)
            modified_ast = ast.parse(modified_code)

            original_functions = {node.name for node in ast.walk(original_ast) if isinstance(node, ast.FunctionDef)}
            modified_functions = {node.name for node in ast.walk(modified_ast) if isinstance(node, ast.FunctionDef)}

            if original_functions != modified_functions:
                logging.warning(f"⚠️ Function structure changed. Original: {original_functions}, Modified: {modified_functions}")

            logging.info("✅ Modification analysis completed. No structural anomalies detected.")
            return True
        except Exception as e:
            logging.error(f"❌ Error during modification analysis: {e}")
            return False

    def validate_ast_modification(self, modified_code):
        """Runs deeper validation on the modified AST to detect anomalies."""
        try:
            tree = ast.parse(modified_code)

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Ensure AI is not modifying critical functions
                    if node.name in ["run", "__init__"]:  
                        logging.error(f"❌ Modification attempt on protected function '{node.name}' detected! Aborting change.")
                        return False

                    # Prevent AI from inserting arbitrary exec() calls
                    for sub_node in ast.walk(node):
                        if isinstance(sub_node, ast.Call) and hasattr(sub_node.func, "id") and sub_node.func.id == "exec":
                            logging.error("❌ Unsafe exec() call detected in modification. Aborting change.")
                            return False

            logging.info("✅ AST validation successful. No unsafe modifications detected.")
            return True
        except Exception as e:
            logging.error(f"❌ AST validation failed: {e}")
            return False
