import ast
import logging
from core_engine.modification.ai_utils import AIUtils

class AIASTParser:
    """Parses and analyzes the AI's own source code using Abstract Syntax Trees (ASTs)."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.utils = AIUtils(file_path)

    def parse_code(self):
        """Reads and parses the AI's source code into an AST."""
        source_code = self.utils.read_source_code()
        try:
            tree = ast.parse(source_code)
            logging.info("✅ Successfully parsed AI's source code into an AST.")
            return tree
        except SyntaxError as e:
            logging.error(f"❌ Syntax error detected in AI's source code: {e}")
            return None

    def extract_function_definitions(self):
        """Extracts function structures from the AI's source code."""
        tree = self.parse_code()
        if not tree:
            return {}

        function_details = {}

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_details[node.name] = {
                    "parameters": len(node.args.args),
                    "num_statements": len(node.body),
                    "contains_loops": any(isinstance(stmt, (ast.For, ast.While)) for stmt in node.body),
                    "contains_conditionals": any(isinstance(stmt, ast.If) for stmt in node.body),
                }

        logging.info(f"📜 Extracted function definitions: {function_details}")
        return function_details
