import shutil
import os
import logging

class AIRollback:
    """Handles error detection and rollback in case of failures."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.backup_path = f"{file_path}.bak"
        
    def create_backup(self):
        """Creates a backup before modification."""
        if not os.path.exists(self.backup_path):
            shutil.copy(self.file_path, self.backup_path)
            logging.info(f"✅ Backup created: {self.backup_path}")
            
    def restore_backup(self):
        """Restores the AI to the last valid state if needed."""
        if os.path.exists(self.backup_path):
            shutil.copy(self.backup_path, self.file_path)
            logging.info("✅ AI restored to last valid version.")
        else:
            logging.warning("⚠️ No backup found. Rollback not possible.")
        