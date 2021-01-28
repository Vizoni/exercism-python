import unittest

from isogram import is_isogram

class IsogramTest(unittest.TestCase):
    def test_no_word(self):
        self.assertIs(is_isogram(''), True) 

    def test_simple_word_not_isogram(self):
        self.assertIs(is_isogram('ovo'), False) 

    def test_simple_word_is_isogram(self):
        self.assertIs(is_isogram('ave'), True)

    def test_word_with_hyphen_is_isogram(self):
        self.assertIs(is_isogram('six-year-old'), True)
        
    def test_word_with_hyphen_not_isogram(self):
        self.assertIs(is_isogram('six-year old'), True)


if __name__ == "__main__":
    unittest.main()