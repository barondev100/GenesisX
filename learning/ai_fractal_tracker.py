import json
import os
import logging

class AIFractalTracker:
    """Tracks recursive function modifications and ensures controlled expansion."""
    LOG_FILE = "fractal_expansion_log.json"
    MAX_EXPANSION_DEPTH = 5  # Prevent infinite recursion

    def __init__(self, file_path):
        self.file_path = file_path
        self.log_data = self._load_log()  # Ensure this method exists with the correct name

    def _load_log(self):
        """Loads function expansion history from a JSON file."""
        if os.path.exists(self.LOG_FILE):
            with open(self.LOG_FILE, "r") as file:
                return json.load(file)
        return {}

    def log_expansion(self, function_name):
        """Logs the number of times a function has expanded."""
        self.log_data[function_name] = self.log_data.get(function_name, 0) + 1
        with open(self.LOG_FILE, "w") as file:
            json.dump(self.log_data, file, indent=4)
        logging.info(f"🔍 Function '{function_name}' expanded to depth {self.log_data[function_name]}")

    def can_expand(self, function_name):
        """Checks if a function has reached its expansion limit."""
        return self.log_data.get(function_name, 0) < self.MAX_EXPANSION_DEPTH
