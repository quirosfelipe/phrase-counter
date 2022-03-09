import unittest
import app

class TestCreateWordList(unittest.TestCase):
    def test_wordList(self):
        data = ['the quick brown fox','jumps over the lazy dog']
        result = app.createWordList(data)
        self.assertEqual(result,['the','quick', 'brown', 'fox','jumps', 'over', 'the', 'lazy', 'dog'])


if __name__ == '__main__':
    unittest.main()