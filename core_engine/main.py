import logging
import os
import sys

# Ensure the core_engine module is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_engine.ai_core import SelfModifyingAI

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format="%(message)s")

if __name__ == "__main__":
    logging.info("🚀 Running Self-Modifying AI...")
    
    # Path to the AI core script
    ai_core_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ai_core.py"))
    
    # Initialize AI
    ai = SelfModifyingAI(ai_core_path)
    
    logging.info("🔍 Analyzing AI source code for inefficiencies...")
    function_report = ai.analyzer.analyze_code()
    
    logging.info("🛠 Applying AI self-optimizations...")
    ai.optimizer.optimize_functions(function_report)

    logging.info("📜 Displaying updated AI source code...")
    ai.reader.display_code()

    logging.info("✅ AI self-modification process completed.")
