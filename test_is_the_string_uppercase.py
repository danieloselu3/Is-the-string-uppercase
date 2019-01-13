import unittest
from is_the_string_uppercase import is_uppercase

class IsUppercaseTestCase(unittest.TestCase):

    def test_is_uppercase_all_uppercase(self):
        string = is_uppercase('ABCDEF')
        self.assertTrue(string)

    def test_is_uppercase_all_lowercase(self):
        string = is_uppercase('abcdef')
        self.assertFalse(string)

    def test_is_uppercase_mixed_uppercase_lowercase(self):
        string = is_uppercase('aBCDef')
        self.assertFalse(string)

    def test_is_uppercase_mixed_character(self):
        string = is_uppercase("HELLO, MY NAME IS !@#$%^&* AND I'M CUTE AS F**K!!!")
        self.assertTrue(string)

    def test_is_uppercase_mixed_character_hidden(self):
        string = is_uppercase("HeLLO !@#$%^&* I LOVe HOw YOU THINK YOUR CUTE AS **SENSORED**")
        self.assertFalse(string)

    def test_is_uppercase_no_alphabet(self):
        string = is_uppercase("!@#$%^&*()_+123456778")
        self.assertTrue(string)

if __name__ == '__main__':
    unittest.main()
