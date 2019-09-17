import unittest

from twitter import tweet_similarity


class MyTestCase(unittest.TestCase):

    def test_are_similar_not_similar(self):
        t1 = 'this is some text about bitcoin #bitcoin'
        t2 = 'nothing similar in it'
        similar = tweet_similarity.are_similar(t1, t2)
        self.assertFalse(similar)

    def test_are_similar_similar_text(self):
        t1 = 'this is some text about bitcoin' + '\n\n' + '#cryptocurrencynews #bitcoin'
        t2 = 'this is some text about bitcoin'
        similar = tweet_similarity.are_similar_text(t1, t2)
        self.assertTrue(similar)

    def test_are_similar(self):
        t1 = 'this is some text about bitcoin #bitcoin'
        t2 = 'this is similar text about bitcoin           #bitcoin'
        similar = tweet_similarity.are_similar(t1, t2)
        self.assertTrue(similar)

    def test_are_similar_source(self):
        s1 = 'this is some text about bitcoin' + '\n\n' \
             + '#cryptocurrencynews #bitcoin' + '\n\n' + 'http://some.domain.net'
        s2 = 'http://some.domain.net'
        similar = tweet_similarity.are_similar_source(s1, s2)
        self.assertTrue(similar)


if __name__ == '__main__':
    unittest.main()
