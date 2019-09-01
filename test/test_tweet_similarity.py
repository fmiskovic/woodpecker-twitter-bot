import unittest

import tweet_similarity


class MyTestCase(unittest.TestCase):

    def test_are_similar(self):
        t1 = 'this is some text about bitcoin #bitcoin'
        t2 = 'this is similar text about bitcoin           #bitcoin'
        similar = tweet_similarity.are_similar(t1, t2)
        self.assertTrue(similar)


if __name__ == '__main__':
    unittest.main()