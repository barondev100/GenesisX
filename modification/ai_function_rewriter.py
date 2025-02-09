import ast
import copy
import logging
import time
import hashlib
from core_engine.execution.ai_sandbox import AISandbox
from core_engine.learning.ai_function_tracker import AIFunctionTracker

class AIFunctionRewriter:
    """Handles recursive function rewriting and adaptive modifications."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.sandbox = AISandbox()
        self.function_tracker = AIFunctionTracker(file_path)

    def analyze_function(self, function_node):
        """Analyze function metrics such as complexity and branching."""
        num_statements = len(function_node.body)
        num_branches = sum(isinstance(node, ast.If) for node in function_node.body)
        return {
            'num_statements': num_statements,
            'num_branches': num_branches,
        }

    def modify_function(self, function_node):
        """Apply adaptive modifications to function logic dynamically."""
        new_node = copy.deepcopy(function_node)

        # Add a logging statement to the start of the function
        logging_stmt = ast.Expr(
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='logging', ctx=ast.Load()),
                    attr='info',
                    ctx=ast.Load()
                ),
                args=[ast.Constant(value=f"Executing {function_node.name} (Modified)")],
                keywords=[]
            )
        )

        new_node.body.insert(0, logging_stmt)
        return new_node

    def evaluate_function(self, function_code):
        """Evaluate the modified function's performance."""
        start_time = time.time()
        try:
            exec(function_code, {})
            execution_time = time.time() - start_time
            return execution_time  # Using execution time as a performance metric
        except Exception as e:
            logging.error(f"Error during function evaluation: {e}")
            return float('inf')  # Penalize functions that raise exceptions

    def rewrite_and_adapt(self):
        """Main method to perform recursive rewriting and adaptive modifications."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            source_code = file.read()

        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                original_metrics = self.analyze_function(node)
                modified_node = self.modify_function(node)
                modified_code = ast.unparse(modified_node)

                if self.function_tracker.has_changed(node.name, modified_code):
                    performance = self.evaluate_function(modified_code)
                    logging.info(f"Function {node.name} - Original Metrics: {original_metrics}, Performance: {performance}")
                    self.function_tracker.log_modification(node.name, modified_code)
                else:
                    logging.info(f"Skipping redundant modification for {node.name}")
