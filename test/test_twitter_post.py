import logging.config
import unittest

import tweets
import twitter_api_auth
from tweets import TweetsHandler

logging.config.fileConfig('logging.config')
logger = logging.getLogger('bot')


class TwitterPostBotTestCases(unittest.TestCase):
    def setUp(self):
        api = twitter_api_auth.create_api()
        self.post_bot = TweetsHandler(api, logging)

    def tearDown(self) -> None:
        super().tearDown()

    def test_create_post(self):
        source = "https://slashdot.org/story/19/05/19/1837257/bitcoin-roars-back-surges-50-in-30-days"
        text = "Bitcoin 'Roars Back', Surges 50% in 30 Days"
        tweet = tweets.create_post(text, source)
        print(tweet)
        self.assertIsNotNone(tweet)

    def test_tweet_news(self):
        source = "https://slashdot.org/story/19/05/19/1837257/bitcoin-roars-back-surges-50-in-30-days"
        text = "Bitcoin 'Roars Back', Surges 50% in 30 Days"

        response = self.post_bot.post_new_tweet(text, source)
        self.assertIsNotNone(response)

    def test_get_latest_tweet(self):
        tweet = self.post_bot.get_latest_tweet()
        self.assertIsNotNone(tweet, msg='You did not get anything')
        self.assertIsNotNone(tweet.text)

    def test_get_tweets_list(self):
        tweet_list = self.post_bot.get_tweets_list(20)

        self.assertIsNotNone(tweet_list)
        self.assertTrue(len(tweet_list) > 0)


if __name__ == '__main__':
    unittest.main()
