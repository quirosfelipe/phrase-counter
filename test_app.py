import unittest
import app

class TestCreateWordList(unittest.TestCase):
    def test_wordList(self):
        data = ['the quick brown fox','jumps over the lazy dog']
        result = app.createWordList(data)
        self.assertEqual(result,['the','quick', 'brown', 'fox','jumps', 'over', 'the', 'lazy', 'dog'])
    def test_mixedCase(self):
        data = ['The quick Brown fox','jumps Over the Lazy dog']
        result = app.createWordList(data)
        self.assertEqual(result,['the','quick', 'brown', 'fox','jumps', 'over', 'the', 'lazy', 'dog'])
    def test_punctuation(self):
        data = ['The ... quick Brown fox.','shouldn\'t jump! Over... the Lazy dog.']
        result = app.createWordList(data)
        self.assertEqual(result,['the','quick', 'brown', 'fox','shouldn\'t','jump', 'over', 'the', 'lazy', 'dog'])
    def test_contractions(self):
        data = ['couldn\'t','shouldn\'t']
        result = app.createWordList(data)
        self.assertEqual(result,['couldn\'t','shouldn\'t'])
    def test_onlyPunctuationString(self):
        data = ['...','!!!','.!.!' ]
        result = app.createWordList(data)
        self.assertEqual(result,[])


if __name__ == '__main__':
    unittest.main()