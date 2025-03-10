import logging
import importlib.util
import os
from core_engine.execution.ai_reader import AIReader
from core_engine.execution.ai_sandbox import AISandbox
from core_engine.learning.ai_learning_manager import AILearningManager
from core_engine.modification.ai_function_rewriter import AIFunctionRewriter
from core_engine.modification.ai_code_expander import AICodeExpander
from core_engine.security.ai_safeguard import AISafeguard
from core_engine.security.ai_security import AISecurity
from core_engine.security.ai_safety import AISafety
from core_engine.security.ai_validation import AIValidation
from core_engine.security.ai_rollback import AIRollback
logging.basicConfig(level=logging.INFO, format='%(message)s')


class SelfModifyingAI:
    """Core AI system that manages self-modification and security."""

    def __init__(self, file_path):
        """Initialize AI system with execution control and security."""
        self.file_path = file_path
        self.learning_manager = AILearningManager(file_path)
        self.function_rewriter = AIFunctionRewriter(file_path)
        self.code_expander = AICodeExpander(file_path)
        self.reader = AIReader(file_path)
        self.sandbox = AISandbox()
        self.safeguard = AISafeguard(file_path)
        self.security = AISecurity()
        self.safety = AISafety()
        self.validation = AIValidation()
        self.rollback = AIRollback(file_path)
        self._load_generated_functions()

    def _load_generated_functions(self):
        """Loads AI-generated functions from `ai_generated.py` dynamically."""
        ai_generated_path = os.path.join(os.path.dirname(__file__),
            'ai_generated.py')
        if os.path.exists(ai_generated_path):
            spec = importlib.util.spec_from_file_location('ai_generated',
                ai_generated_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.ai_generated_module = module
            logging.info('✅ AI-generated functions successfully loaded!')
        else:
            logging.warning('⚠️ No AI-generated functions found.')

    def run(self):
        """Runs the AI engine, ensuring integrity and self-improvement."""
        logging.info('🚀 Starting AI execution...')
        if not self.safety.check_recursion_depth():
            logging.error('⚠️ Infinite recursion detected! Halting execution.')
            return
        logging.info('🔄 Running AI Learning Cycle...')
        self.learning_manager.run_learning_cycle()
        logging.info('🔄 Running Recursive Function Rewriting...')
        modified_functions = self.function_rewriter.rewrite_and_adapt()
        if not modified_functions:
            logging.info(
                '✅ No significant changes detected, skipping modifications.')
        logging.info('🔁 AI is generating new functions dynamically...')
        expanded_function = self.code_expander.expand_code()
        if expanded_function:
            logging.info(
                f'✅ Successfully expanded new function `{expanded_function}`.')
        else:
            logging.info('⚠️ No new functions were generated. Debug required!')
        logging.info('🔍 Validating modified AI source code...')
        if not self.validation.validate_code(self.file_path):
            logging.error('❌ Code validation failed. Aborting modification.')
            return
        logging.info('🛠 Creating backup before applying modifications...')
        self.rollback.create_backup()
        logging.info('🔍 Running post-modification corruption check...')
        if not self.safeguard.monitor_execution(self.run):
            logging.error(
                '⚠️ AI corruption detected. Restoring previous stable version.'
                )
            return
        logging.info('📜 Displaying modified AI source code...')
        self.reader.display_code()


if __name__ == '__main__':
    ai = SelfModifyingAI(__file__)
    ai.run()
