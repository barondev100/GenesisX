import ast
import astor  # type: ignore
import logging
from core_engine.modification.ai_utils import AIUtils
from core_engine.modification.ai_ast_parser import AIASTParser  # Centralized AST processing

class AIModifier:
    """Forcefully modifies AI functions using AST to ensure real self-modification."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.utils = AIUtils(file_path)
        self.ast_parser = AIASTParser(file_path)  # Use centralized AST processing

    def modify_function(self, function_name, new_code=None):
        """Modifies only the target function without overwriting the entire file."""
        tree = self.ast_parser.parse_code()  # Get AST from centralized parser
        if not tree:
            logging.error("❌ AST Parsing failed. Aborting modification.")
            return False

        class FunctionRewriter(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.name == function_name:
                    logging.info(f"🔄 Found '{function_name}', modifying...")

                    try:
                        # Ensure proper indentation
                        if new_code:
                            parsed_code = ast.parse(new_code).body
                            for stmt in parsed_code:
                                ast.increment_lineno(stmt, node.lineno)  # Adjust line numbers
                                if hasattr(stmt, 'col_offset'):
                                    stmt.col_offset = node.body[0].col_offset if node.body else 4  # Match indentation level
                        else:
                            parsed_code = [ast.Pass()]  # Placeholder if no new code

                        # Replace function body with properly formatted new code
                        node.body = [
                            ast.Expr(ast.Constant(s=f"MODIFIED: AI has rewritten {function_name}"))
                        ] + parsed_code

                        logging.info(f"✅ Successfully modified '{function_name}'.")

                    except SyntaxError as e:
                        logging.error(f"❌ Failed to modify '{function_name}': Syntax error in new code → {e}")
                        return node

                return node

        # Apply AST transformation
        modified_tree = FunctionRewriter().visit(tree)
        modified_code = astor.to_source(modified_tree)

        # Prevent accidental overwrites by ensuring function still exists
        if function_name not in modified_code:
            logging.error(f"❌ Function '{function_name}' is missing in modified AST. Aborting write.")
            return False

        # Backup before modifying the file
        self.utils.create_backup()
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(modified_code)

        logging.info(f"✅ Successfully modified '{function_name}' while preserving other functions.")
        return True
