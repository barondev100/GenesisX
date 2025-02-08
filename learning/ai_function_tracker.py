import json
import os
import logging
import hashlib

class AIFunctionTracker:
    """Tracks function modifications across multiple iterations and compares versions."""

    LOG_FILE = "function_modifications.json"

    def __init__(self, file_path):
        self.file_path = file_path
        self.function_data = self._load_log()

    def _load_log(self):
        """Loads function modification history from a JSON file."""
        if os.path.exists(self.LOG_FILE):
            with open(self.LOG_FILE, "r") as file:
                return json.load(file)
        return {}

    def log_modification(self, function_name, new_code):
        """Logs a function modification, storing its hash to track changes."""
        code_hash = hashlib.sha256(new_code.encode()).hexdigest()
        self.function_data[function_name] = {
            "modification_count": self.function_data.get(function_name, {}).get("modification_count", 0) + 1,
            "last_hash": code_hash
        }
        with open(self.LOG_FILE, "w") as file:
            json.dump(self.function_data, file, indent=4)
        logging.info(f"📝 Function '{function_name}' modified. Total modifications: {self.function_data[function_name]['modification_count']}")

    def has_changed(self, function_name, new_code):
        """Checks if a function has changed by comparing its hash."""
        code_hash = hashlib.sha256(new_code.encode()).hexdigest()
        return self.function_data.get(function_name, {}).get("last_hash") != code_hash
