import logging
import traceback
from core_engine.security.ai_rollback import AIRollback

class AISafeguard:
    """Monitors AI execution to detect instability and prevent self-corruption."""

    def __init__(self, file_path):
        """Initialize safeguard system with rollback capability."""
        self.file_path = file_path
        self.rollback = AIRollback(file_path)

    def monitor_execution(self, execution_function):
        """
        Monitors AI execution after modifications. If execution fails,
        it logs the error and triggers a rollback.
        """
        try:
            execution_function()  # Run the AI execution process
            logging.info("✅ AI executed successfully. No corruption detected.")
            return True
        except Exception as e:
            error_details = traceback.format_exc()
            logging.error(f"❌ AI execution failure detected: {e}\n{error_details}")
            logging.info("🔄 Rolling back to last stable version due to corruption.")
            self.rollback.restore_backup()
            return False
