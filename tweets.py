import logging.config

logging.config.fileConfig('logging.config')
logger = logging.getLogger(__name__)


def create_post(text, source):
    logger.info('Creating twitter post text...')
    return text + '\n\n' + '#cryptocurrencynews #cryptocurrency #blockchain #bitcoin ' \
                           '#crypto #btc #ltc #ethereum #litecoin' + '\n\n' + source


class TweetsHandler:
    """Use this class to handle or manage tweets"""

    def __init__(self, tw_api):
        logger.info('Initializing TweetsHandler')
        self.api = tw_api
        self.me = self.api.me()

    def post_new_tweet(self, text, source):
        """Tweet some news"""
        latest_tweets = self.get_tweets_list(20)
        text = create_post(text, source)
        if len(latest_tweets) > 0:
            for t in latest_tweets:
                if text == t.text:
                    logger.info('You already tweeted this. I do not want to tweet duplicate.')
                    return None

        logger.info('Posting a new tweet...')
        return self.api.update_status(text)

    def get_latest_tweet(self):
        logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=1)[0]

    def get_tweets_list(self, size):
        logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=size)
