import pytest
import math
from mypackage.calculator import add, subtract, multiply, divide, power, root, sin, cos, tan
'''
Develop a unit testing plan for the following project: 
a command-line engineering calculator that 
includes the four basic arithmetic operations, power, root, 
and trigonometric functions (sine, cosine, and tangent). 
Share the GitHub link including the code and short description.
'''

# Test 2^3 = 8 and 27^(1/3) = 3
def test_power():
    assert power(2, 3) == 8
def test_root():
    assert math.isclose(root(27, 1/3), 3, rel_tol=1e-9)

# Test trigonometric functions
'''
math.isclose is used to compare floating-point numbers
If the result is close to the expected values, allowing for small floating-point inaccuracies.
rel_tol is the relative tolerance.
le-9 means the numbers can differ by up to 1 part in 1,000,000,000.
'''
# Test sin(90) = 1, cos(0) = 1, tan(45) = 1
def test_sin():
    assert math.isclose(sin(math.pi/2), 1, rel_tol=1e-9)
def test_cos():
    assert math.isclose(cos(0), 1, rel_tol=1e-9)
def test_tan():
    assert math.isclose(tan(math.pi/4), 1, rel_tol=1e-9)

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

if __name__ == "__main__":
    pytest.main()
