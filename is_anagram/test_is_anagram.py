import unittest

from is_anagram import is_anagram


class AnagramTest(unittest.TestCase):

    def test_anagram_false(self):
        self.assertIs(is_anagram('row', 'bow'), False)

    def test_anagram_true(self):
        self.assertIs(is_anagram('dog', 'god'), True)

    def test_anagram_not_equal_letters(self):
        self.assertIs(is_anagram('Hamster Jones', 'Hamster'), False)

    def test_anagram_different_casing(self):
        self.assertIs(is_anagram('RaCe C  Ar', 'racecar'), True)


if __name__ == '__main__':
    unittest.main()
