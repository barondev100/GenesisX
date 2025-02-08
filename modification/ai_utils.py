import os
import logging

class AIUtils:
    def __init__(self, file_path):
        """Initialize AI Utilities with the file path."""
        self.file_path = file_path
    def read_source_code(self):
        """Reads the AI's own source code safely."""
        self.file_path = os.path.abspath(self.file_path)  # Ensure absolute path
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()
    def create_backup(self):
        """Creates a backup of the original source file before modification."""
        backup_path = self.file_path + ".bak"
        if os.path.exists(self.file_path):  # Ensure file exists before renaming
            with open(self.file_path, "r", encoding="utf-8") as original, open(backup_path, "w", encoding="utf-8") as backup:
                backup.write(original.read())  # Copy file content instead of renaming
            logging.info(f"✅ Backup created: {backup_path}")

    def restore_backup(self):
        """Restores the backup if needed."""
        backup_path = self.file_path + ".bak"
        if os.path.exists(backup_path):
            os.rename(backup_path, self.file_path)
            logging.info("✅ Backup restored.")
        else:
            logging.warning("⚠️ No backup found to restore.")