import json
import hashlib
import logging

class AIFunctionTracker:
    """Tracks function modifications across iterations."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.log_file = "function_modifications.json"
        self.data = self._load_log()

    def _load_log(self):
        """Load existing function modification logs."""
        try:
            with open(self.log_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning("⚠️ Corrupt JSON file detected. Resetting log...")
            return {}

    def has_changed(self, function_name, function_code):
        """Check if the function has been modified since last iteration."""
        if function_name not in self.data:
            return True  # New function

        # ✅ FIX: Convert dict function_code into a string before hashing
        function_code_str = json.dumps(function_code, sort_keys=True)

        function_hash = hashlib.sha256(function_code_str.encode()).hexdigest()
        return self.data[function_name]["last_hash"] != function_hash

    def log_modification(self, function_name, function_code):
        """Logs function modifications."""
        function_code_str = json.dumps(function_code, sort_keys=True)
        function_hash = hashlib.sha256(function_code_str.encode()).hexdigest()

        self.data[function_name] = {
            "modification_count": self.data.get(function_name, {}).get("modification_count", 0) + 1,
            "last_hash": function_hash
        }

        with open(self.log_file, "w") as file:
            json.dump(self.data, file, indent=4)
