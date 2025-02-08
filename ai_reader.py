import logging
from core_engine.ai_utils import AIUtils  # Use centralized file handling

class AIReader:
    """Handles reading and displaying AI's source code."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.utils = AIUtils(file_path)  # Use centralized file handler

    def display_code(self):
        """Displays the AI's own code."""
        try:
            source_code = self.utils.read_source_code()  # Read using AIUtils
            logging.info(f"📜 AI source code:\n" + "-" * 40)
            logging.info(source_code.strip())
        except Exception as e:
            logging.error(f"Error reading file: {e}")
