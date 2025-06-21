import unittest

def add(x,y):
    return x + y


'''
This is a unit test of the add function.
It checks if the result of add(x,y) matches the expected value.
'''
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # add(2,3) = 5 and expected value is 5
        self.assertEqual(add(2, 3), 5)
        # add(-1,1) = 0 and expected value is 0
        self.assertEqual(add(-1, 1), 0)

        # Fail case: add(2,-1) = 1 and expected value is 4
        self.assertEqual(add(2, -1), 4)       

if __name__ == "__main__":
    unittest.main()
