import logging
from core_engine.learning.ai_fpl import AIFPL
from core_engine.learning.ai_fractal_tracker import AIFractalTracker
from core_engine.learning.ai_function_tracker import AIFunctionTracker
from core_engine.learning.ai_optimizer import AIOPTimizer
from core_engine.learning.ai_analyzer import AIAnalyzer
from core_engine.modification.ai_modifier import AIModifier

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

    def run_learning_cycle(self):
        """Executes AI fractal learning and tracks function evolution."""
        logging.info("🚀 Running AI Fractal Learning Expansion...")
        self.fpl.analyze_and_expand()

        function_report = self.analyzer.analyze_code()

        for function_name in function_report:
            if self.fractal_tracker.can_expand(function_name):
                self.fractal_tracker.log_expansion(function_name)
            if not self.function_tracker.has_changed(function_name, "dummy_code"):
                logging.info(f"🔄 Skipping redundant modification for '{function_name}', no significant change detected.")

        logging.info("🔍 Analyzing AI source code for inefficiencies...")
        self.optimizer.optimize_functions(function_report)

        logging.info("✅ AI Learning Cycle Completed.")
