import logging
import os
import sys
import importlib.util

# Prevent Python from creating __pycache__ and .pyc files
sys.dont_write_bytecode = True  # Disables .pyc file creation globally
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"  # Ensures it applies across imports

# Ensure the core_engine module is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_engine.ai_core import SelfModifyingAI

# Remove any existing __pycache__ directories if they exist
def remove_pycache(root_dir):
    """Recursively remove all __pycache__ folders from core_engine."""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "__pycache__" in dirnames:
            pycache_path = os.path.join(dirpath, "__pycache__")
            for filename in os.listdir(pycache_path):
                os.remove(os.path.join(pycache_path, filename))  # Remove .pyc files
            os.rmdir(pycache_path)  # Remove empty __pycache__ folder
            logging.info(f"🗑 Removed: {pycache_path}")

# Call the function to clean __pycache__
remove_pycache(os.path.abspath(os.path.dirname(__file__)))

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format="%(message)s")

if __name__ == "__main__":
    logging.info("🚀 Running Self-Modifying AI...")

    # Path to the AI core script
    ai_core_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ai_core.py"))

    # Initialize AI
    ai = SelfModifyingAI(ai_core_path)

    logging.info("🔄 Running AI Fractal Learning Expansion...")
    ai.fpl.analyze_and_expand()  # NEW: Run fractal propagation learning

    logging.info("🔍 Analyzing AI source code for inefficiencies...")
    function_report = ai.analyzer.analyze_code()

    logging.info("🛠 Applying AI self-optimizations...")
    ai.optimizer.optimize_functions(function_report)

    logging.info("📜 Displaying updated AI source code...")
    ai.reader.display_code()

    logging.info("✅ AI self-modification process completed.")
