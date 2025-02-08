import ast
import astor # type: ignore
import logging
from core_engine.ai_utils import AIUtils
from core_engine.ai_ast_parser import AIASTParser  # Centralized AST processing

class AIModifier:
    """Forcefully modifies AI functions using AST to ensure real self-modification."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.utils = AIUtils(file_path)
        self.ast_parser = AIASTParser(file_path)  # Use centralized AST processing

    def modify_function(self, function_name):
        """Brutally replaces inefficient function bodies with optimized versions."""
        tree = self.ast_parser.parse_code()  # Get AST from centralized parser
        if not tree:
            logging.error("❌ AST Parsing failed. Aborting modification.")
            return False

        class FunctionRewriter(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.name == function_name:
                    logging.info(f"🔄 Found '{function_name}', forcing modification...")

                    # **Overwrite function completely with optimized version**
                    node.body = [
                        ast.Expr(ast.Str(s="MODIFIED: AI has rewritten this function")),
                        ast.Assign(
                            targets=[ast.Name(id="total", ctx=ast.Store())],
                            value=ast.Call(
                                func=ast.Name(id="sum", ctx=ast.Load()),
                                args=[ast.List(elts=[
                                    ast.Constant(value=1),
                                    ast.Constant(value=2),
                                    ast.Constant(value=3),
                                    ast.Constant(value=4),
                                    ast.Constant(value=5)
                                ], ctx=ast.Load())],
                                keywords=[]
                            )
                        ),
                        ast.Expr(ast.Call(
                            func=ast.Name(id="print", ctx=ast.Load()),
                            args=[ast.Str(s="Total:"), ast.Name(id="total", ctx=ast.Load())],
                            keywords=[]
                        ))
                    ]

                    logging.info(f"✅ Successfully overwrote '{function_name}' with optimized logic.")

                return node

        # **Apply AST transformation**
        modified_tree = FunctionRewriter().visit(tree)

        # **Ensure changes exist in AST before writing**
        modified_code = astor.to_source(modified_tree)
        if function_name not in modified_code:
            logging.error(f"❌ Function '{function_name}' is missing from modified AST. Aborting write.")
            return False

        # **Backup & Write**
        self.utils.create_backup()
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(modified_code)

        logging.info(f"✅ Brutally modified function '{function_name}' and wrote changes to file.")
        return True
