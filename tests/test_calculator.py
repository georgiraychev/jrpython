import pytest
from interview.problem import BrokenCalculator

def test_addition():
    calc = BrokenCalculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_multiplication():
    calc = BrokenCalculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0 