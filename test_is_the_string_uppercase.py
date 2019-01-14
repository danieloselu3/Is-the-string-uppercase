#import unittest
import unittest

#import/define method to be tested
from is_the_string_uppercase import is_uppercase


class IsUppercaseTestCase(unittest.TestCase):
    #method 1
    def test_is_uppercase_all_uppercase(self):
        string = is_uppercase('ABCDEF')
        self.assertTrue(string)

    #method 2
    def test_is_uppercase_all_lowercase(self):
        string = is_uppercase('abcdef')
        self.assertFalse(string)

    #method 3
    def test_is_uppercase_mixed_uppercase_lowercase(self):
        string = is_uppercase('aBCDef')
        self.assertFalse(string)

    #method 4
    def test_is_uppercase_mixed_character(self):
        string = is_uppercase("HELLO, MY NAME IS !@#$%^&* AND I LOVE FOOD.")
        self.assertTrue(string)

    #method 5
    def test_is_uppercase_mixed_character_hidden(self):
        string = is_uppercase("HeLLO !@#$%^&* I LOVe FooD tOO.")
        self.assertFalse(string)

    #method 6
    def test_is_uppercase_no_alphabet(self):
        string = is_uppercase("!@#$%^&*()_+123456778")
        self.assertTrue(string)

    #method 7
    def test_is_uppercase_empty_string(self):
        string = is_uppercase('')
        self.assertTrue(string)

#make the script executable using if-name-main
if __name__ == '__main__':
    unittest.main()
