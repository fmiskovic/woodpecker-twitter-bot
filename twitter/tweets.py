import logging.config

from twitter import tweet_similarity


def create_post(text, source, hashtag='#cryptocurrency'):
    if len(text) >= 170:
        sub_text = text[0:166] + '...'
        return sub_text + '\n\n' + hashtag + '\n\n' + source
    else:
        return text + '\n\n' + hashtag + '\n\n' + source


class TweetsHandler:
    """Use this class to handle or manage tweets"""

    def __init__(self, tw_api):
        self.api = tw_api
        self.me = self.api.me()

        self.logger = logging.getLogger(__name__)
        self.logger.info('Initialized TweetsHandler')

    def post_new_tweet(self, text, source, hashtag=None):
        """Tweet some news"""
        latest_tweets = self.get_tweets_list(20)
        if len(latest_tweets) > 0:
            for t in latest_tweets:
                if tweet_similarity.are_similar_source(t.text, source):
                    self.logger.info('Found duplicated news by source. I do not want to tweet duplicate.')
                    return None
                elif tweet_similarity.are_similar_text(t.text, text):
                    self.logger.info('Found duplicated news by text. I do not want to tweet duplicate.')
                    return None

        try:
            self.logger.info('Posting a new tweet...')
            return self.api.update_status(create_post(text, source, hashtag))
        except Exception as e:
            self.logger.error('Failed to post new tweet: %s', e, exc_info=1)
            return None

    def get_latest_tweet(self):
        self.logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=1)[0]

    def get_tweets_list(self, size):
        self.logger.info('Getting my last tweet...')
        return self.api.user_timeline(id=self.me.id, count=size)
