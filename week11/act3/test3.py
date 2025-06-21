import unittest
'''
Tasks to do:
Describe what each test method is checking.
Run the code and interpret the results.
Modify the code to add a new test case that checks if '123'.isdigit() returns True.
What happens if one of the assertions fails? 
Try changing one expected value and observe the result.
'''

class TestStringMethods(unittest.TestCase):
    
    def test_digit(self):
        # Test if the string '123' is a digit.
        # It should return True.
        self.assertTrue('123'.isdigit())
        # Fail case: 'digit' is not a digit, should return False.
        self.assertTrue('digit'.isdigit())

    # Test the string upper 'foo' is converted to uppercase 'FOO'.
    def test_upper(self):

        # Fail case: 'foo' should be converted to 'FOO' not 'Foo'.
        self.assertEqual('foo'.upper(), 'Foo')
    
    # Test the string 'FOO' and 'Foo' if they are uppercase.
    # 'FOO' should return True, 'Foo' should return False.
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    # Test the split the string 'hello world' into a list of words.
    # It should return ['hello', 'world'].
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()