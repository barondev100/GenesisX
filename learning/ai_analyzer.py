import logging
from core_engine.modification.ai_utils import AIUtils
from core_engine.modification.ai_ast_parser import AIASTParser  # Import AST parser

class AIAnalyzer:
    """Analyzes AI's source code for inefficiencies."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.utils = AIUtils(file_path)
        self.ast_parser = AIASTParser(file_path)  # Use centralized AST processing

    def analyze_code(self):
        """Analyzes functions for inefficiencies using AST."""
        function_details = self.ast_parser.extract_function_definitions()
        logging.info(f"🔍 Function analysis completed: {function_details}")
        return function_details
