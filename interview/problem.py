class BrokenCalculator:
    """
    This calculator has some bugs that need to be fixed.
    The candidate should make all tests pass.
    """
    def add(self, a, b):
        # Bug: Incorrect addition
        return a - b  # This should be fixed by candidate
    
    def multiply(self, a, b):
        # Bug: Incorrect multiplication
        return a + b  # This should be fixed by candidate 