import sys

class AISafety:
    """Prevents infinite recursion and execution crashes."""
    
    MAX_RECURSION_DEPTH = 5 #Adjust based on AI complexity
    
    def __init__(self):
        self.current_depth = 0
        
    def check_recursion_depth(self):
        """Prevents infinite modfication loops."""
        if self.current_depth > self.MAX_RECURSION_DEPTH:
            return False
        self.current_depth += 1
        return True