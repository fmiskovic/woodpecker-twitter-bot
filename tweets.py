import tweet_similarity


def create_post(text, source):
    return text + '\n\n' + '#cryptocurrencynews #cryptocurrency #blockchain #bitcoin ' \
                           '#crypto #btc #ltc #ethereum #litecoin' + '\n\n' + source


class TweetsHandler:
    """Use this class to handle or manage tweets"""

    def __init__(self, tw_api, logger):
        self.logger = logger
        self.api = tw_api
        self.me = self.api.me()
        logger.info('Initialized TweetsHandler')

    def post_new_tweet(self, text, source):
        """Tweet some news"""
        latest_tweets = self.get_tweets_list(100)
        text = create_post(text, source)
        if len(latest_tweets) > 0:
            for t in latest_tweets:
                if tweet_similarity.are_similar(t.text, text):
                    self.logger.info('You already tweeted this. I do not want to tweet duplicate.')
                    return None

        self.logger.info('Posting a new tweet...')
        try:
            return self.api.update_status(text)
        except Exception as e:
            self.logger.error('Failed to post new tweet: %s', e, exc_info=1)

    def get_latest_tweet(self):
        self.logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=1)[0]

    def get_tweets_list(self, size):
        self.logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=size)
