# This file makes core_engine a package
# It allows importing modules from core_engine

from core_engine.ai_core import SelfModifyingAI
from core_engine.ai_reader import AIReader
from core_engine.ai_modifier import AIModifier
from core_engine.ai_analyzer import AIAnalyzer
from core_engine.ai_optimizer import AIOPTimizer
from core_engine.ai_utils import AIUtils
from core_engine.ai_reflector import AIReflector  # NEW: AI Reflection for Runtime Evaluation
from core_engine.ai_sandbox import AISandbox  # NEW: AI Sandbox for Safe Execution

# NEW IMPORTS FOR SECURITY
from core_engine.security.ai_safety import AISafety
from core_engine.security.ai_validation import AIValidation
from core_engine.security.ai_rollback import AIRollback
from core_engine.security.ai_safeguard import AISafeguard  # NEW: AI Self-Corruption Prevention
