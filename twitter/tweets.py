import logging.config

from twitter import tweet_similarity


def create_post(text, source):
    hashtags = '#cryptocurrencynews #cryptocurrency #bitcoin $BTC #BTC #LTC #ETH #XRP'
    if len(text) >= 140:
        sub_text = text[0:136] + '...'
        return sub_text + '\n\n' + hashtags + '\n\n' + source
    else:
        return text + '\n\n' + hashtags + '\n\n' + source


class TweetsHandler:
    """Use this class to handle or manage tweets"""

    def __init__(self, tw_api):
        self.api = tw_api
        self.me = self.api.me()

        logging.config.fileConfig('logging.config')
        self.logger = logging.getLogger('tw')
        self.logger.info('Initialized TweetsHandler')

    def post_new_tweet(self, text, source):
        """Tweet some news"""
        latest_tweets = self.get_tweets_list(100)
        if len(latest_tweets) > 0:
            for t in latest_tweets:
                if tweet_similarity.are_similar_text(t.text, text):
                    self.logger.info('You already tweeted this. I do not want to tweet duplicate.')
                    return None

        try:
            self.logger.info('Posting a new tweet...')
            return self.api.update_status(create_post(text, source))
        except Exception as e:
            self.logger.error('Failed to post new tweet: %s', e, exc_info=1)

    def get_latest_tweet(self):
        self.logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=1)[0]

    def get_tweets_list(self, size):
        self.logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=size)
