import logging
from core_engine.learning.ai_fpl import AIFPL
from core_engine.learning.ai_fractal_tracker import AIFractalTracker
from core_engine.learning.ai_function_tracker import AIFunctionTracker
from core_engine.learning.ai_optimizer import AIOPTimizer
from core_engine.learning.ai_analyzer import AIAnalyzer
from core_engine.modification.ai_modifier import AIModifier
from core_engine.modification.ai_code_expander import AICodeExpander  # ✅ NEW: Dynamic Function Generation

class AILearningManager:
    """Handles AI fractal learning, function tracking, and optimization."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.fpl = AIFPL(file_path)  # Fractal Propagation Learning
        self.fractal_tracker = AIFractalTracker(file_path)  # Tracks recursive learning layers
        self.function_tracker = AIFunctionTracker(file_path)  # Tracks function modifications across iterations
        self.analyzer = AIAnalyzer(file_path)
        self.optimizer = AIOPTimizer(file_path)
        self.modifier = AIModifier(file_path)
        self.code_expander = AICodeExpander(file_path)  # ✅ NEW: AI Function Expansion

    def run_learning_cycle(self):
        """Executes AI fractal learning, tracks function evolution, and dynamically expands AI functions."""
        logging.info("🚀 Running AI Fractal Learning Expansion...")
        self.fpl.analyze_and_expand()

        function_report = self.analyzer.analyze_code()

        for function_name, function_code in function_report.items():
            # ✅ NEW: Expand AI-generated functions dynamically
            if self.fractal_tracker.can_expand(function_name):
                self.fractal_tracker.log_expansion(function_name)

            # ✅ NEW: Generate and track AI functions dynamically
            if self.function_tracker.has_changed(function_name, function_code):
                self.function_tracker.log_modification(function_name, function_code)
                logging.info(f"📝 Function '{function_name}' modified and logged.")
            else:
                logging.info(f"🔄 Skipping redundant modification for '{function_name}', no significant change detected.")

        # ✅ NEW: Generate new AI functions dynamically
        new_functions = self.code_expander.expand_code()
        if new_functions:
            logging.info(f"✅ AI successfully expanded {len(new_functions)} new functions.")

        logging.info("🔍 Analyzing AI source code for inefficiencies...")
        self.optimizer.optimize_functions(function_report)

        logging.info("✅ AI Learning Cycle Completed.")
