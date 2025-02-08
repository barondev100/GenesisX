import logging
from core_engine.execution.ai_reader import AIReader
from core_engine.execution.ai_sandbox import AISandbox
from core_engine.learning.ai_learning_manager import AILearningManager  # NEW
from core_engine.security.ai_safeguard import AISafeguard
from core_engine.security.ai_security import AISecurity
from core_engine.security.ai_safety import AISafety
from core_engine.security.ai_validation import AIValidation
from core_engine.security.ai_rollback import AIRollback

logging.basicConfig(level=logging.INFO, format="%(message)s")

class SelfModifyingAI:
    """Core AI system that manages self-modification and security."""

    def __init__(self, file_path):
        """Initialize AI system with execution control and security."""
        self.file_path = file_path
        self.learning_manager = AILearningManager(file_path)  # Handles Learning & Optimization
        self.reader = AIReader(file_path)
        self.sandbox = AISandbox()
        self.safeguard = AISafeguard(file_path)
        self.security = AISecurity()
        self.safety = AISafety()
        self.validation = AIValidation()
        self.rollback = AIRollback(file_path)

    def run(self):
        """Runs the AI engine, ensuring integrity and self-improvement."""
        logging.info("🚀 Starting AI execution...")

        # Prevent infinite recursion loops
        if not self.safety.check_recursion_depth():
            logging.error("⚠️ Infinite recursion detected! Halting execution.")
            return

        # **NEW: Run AI Learning Manager**
        self.learning_manager.run_learning_cycle()

        # Validate before modifying
        if not self.validation.validate_code(self.file_path):
            logging.error("❌ Code validation failed. Aborting modification.")
            return

        # Backup before modification
        self.rollback.create_backup()

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

