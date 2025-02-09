import ast
import random
import logging
import json
import hashlib
import os
from core_engine.execution.ai_sandbox import AISandbox
from core_engine.learning.ai_function_tracker import AIFunctionTracker

class AICodeExpander:
    """Handles AI-generated function expansion while maintaining code stability."""

    FUNCTION_TEMPLATES = [
        """def {name}():
    print('Executing AI-generated function {name}.')
    return {value}""",
        """def {name}(x):
    print('Executing AI-generated function {name} with input:', x)
    return x * {value}""",
        """def {name}(x, y):
    print('Executing AI-generated function {name} with values:', x, y)
    return (x + y) * {value}"""
    ]

    def __init__(self, file_path):
        self.file_path = file_path
        self.generated_functions_file = os.path.join(os.path.dirname(file_path), "ai_generated.py")
        self.sandbox = AISandbox()
        self.function_tracker = AIFunctionTracker(file_path)
        self.generated_functions = []

    def generate_function(self):
        """Generates a new function dynamically."""
        function_name = f"ai_generated_{random.randint(1000, 9999)}"
        template = random.choice(self.FUNCTION_TEMPLATES)
        value = random.randint(1, 100)
        function_code = template.format(name=function_name, value=value)

        if self.function_tracker.has_changed(function_name, function_code):
            self.function_tracker.log_modification(function_name, function_code)
            logging.info(f"\n📝 **New AI-Generated Function:**\n{function_code}\n")
            self.generated_functions.append(function_name)
        else:
            logging.info(f"🔄 Skipping duplicate function: {function_name}")

        return function_name, function_code

    def inject_function(self, function_name, function_code):
        """Injects the generated function into `ai_generated.py` without modifying core files."""
        try:
            with open(self.generated_functions_file, "a", encoding="utf-8") as f:
                f.write("\n" + function_code + "\n")

            logging.info(f"✅ AI-generated function `{function_name}` successfully injected into `ai_generated.py`.")

        except Exception as e:
            logging.error(f"❌ Function injection failed: {e}")

    def expand_code(self):
        """Creates, injects, and logs AI-generated functions dynamically."""
        function_name, new_function_code = self.generate_function()
        if new_function_code:
            logging.info(f"🔬 Injecting AI-generated function `{function_name}`...")
            self.inject_function(function_name, new_function_code)
            return function_name
        return None
