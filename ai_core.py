import logging
from core_engine.execution.ai_reader import AIReader
from core_engine.modification.ai_modifier import AIModifier
from core_engine.learning.ai_analyzer import AIAnalyzer
from core_engine.learning.ai_optimizer import AIOPTimizer
from core_engine.modification.ai_utils import AIUtils
from core_engine.learning.ai_reflector import AIReflector
from core_engine.execution.ai_sandbox import AISandbox
from core_engine.security.ai_safeguard import AISafeguard
from core_engine.security.ai_security import AISecurity
from core_engine.learning.ai_fpl import AIFPL
from core_engine.learning.ai_fractal_tracker import AIFractalTracker
from core_engine.security.ai_safety import AISafety
from core_engine.security.ai_validation import AIValidation
from core_engine.security.ai_rollback import AIRollback

logging.basicConfig(level=logging.INFO, format="%(message)s")

class SelfModifyingAI:
    """Core AI system capable of self-modification using AST-based function rewriting."""

    def __init__(self, file_path):
        """Initialize AI system with function tracking, self-improvement, and security layers."""
        self.file_path = file_path
        self.fpl = AIFPL(file_path)  # Fractal Propagation Learning
        self.fractal_tracker = AIFractalTracker(file_path) # Tracks recursive learning layers
        self.reader = AIReader(file_path)
        self.modifier = AIModifier(file_path)
        self.analyzer = AIAnalyzer(file_path)
        self.optimizer = AIOPTimizer(file_path)
        self.utils = AIUtils(file_path)
        self.reflector = AIReflector(self)
        self.sandbox = AISandbox()
        self.safeguard = AISafeguard(file_path)
        self.security = AISecurity()
        self.safety = AISafety()
        self.validation = AIValidation()
        self.rollback = AIRollback(file_path)

    def run(self):
        """Runs the AI engine, ensuring integrity and applying recursive learning."""
        logging.info("🚀 Starting AI self-analysis...")

        # Prevent infinite recursion loops
        if not self.safety.check_recursion_depth():
            logging.error("⚠️ Infinite recursion detected! Halting execution.")
            return

        function_report = self.analyzer.analyze_code()

        # **NEW: Run Fractal Learning Expansion**
        logging.info("🚀 Running AI Fractal Learning Expansion...")
        self.fpl.analyze_and_expand()
        
        # Track function history and recursive depth
        for function_name in function_report:
            if self.fractal_tracker.can_expand(function_name):
                self.fractal_tracker.log_expansion(function_name)

        # Retrieve function reflection data before modifying
        for function_name in function_report:
            function_info = self.reflector.get_function_info(function_name)
            if function_info:
                logging.info(f"🔍 Reflecting on function '{function_name}': {function_info}")

        # Validate before modifying
        if not self.validation.validate_code(self.file_path):
            logging.error("❌ Code validation failed. Aborting modification.")
            return

        # Backup before modification
        self.rollback.create_backup()

        logging.info("🔧 Applying AI self-optimizations...")
        try:
            for function_name in function_report:
                # Generate modification code dynamically
                modification_code = f"print('🔧 AI modifying function: {function_name}')"

                # Test modification in sandbox before applying
                if not self.sandbox.test_code(modification_code):
                    logging.error(f"❌ Modification rejected for '{function_name}'. Sandbox test failed.")
                    continue  # Skip modification if it fails sandbox execution

                # Enforce security policies before modifying
                if not self.security.enforce_security_policies(modification_code):
                    logging.error(f"❌ Security policy violation. Modification rejected for '{function_name}'.")
                    continue  # Skip modification if it violates security rules

                # Apply optimization logic
                self.optimizer.optimize_functions(function_report)

        except Exception as e:
            logging.error(f"❌ Modification failed: {e}")
            logging.info("🔄 Rolling back to previous version...")
            self.rollback.restore_backup()
            return

        # **NEW: Monitor execution for corruption**
        logging.info("🔍 Running post-modification corruption check...")
        if not self.safeguard.monitor_execution(self.run):
            logging.error("⚠️ AI corruption detected. Restoring previous stable version.")
            return

        logging.info("📜 Displaying modified AI source code...")
        self.reader.display_code()


if __name__ == "__main__":
    ai = SelfModifyingAI(__file__)
    ai.run()
