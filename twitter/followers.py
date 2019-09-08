import logging.config

import tweepy


class FollowersHandler:

    def __init__(self, tw_api):

        self.api = tw_api
        self.me = self.api.me()

        self.logger = logging.getLogger(__name__)
        self.logger.info('Initializing FollowersHandler')

    def follow_followers(self):
        self.logger.info("Retrieving and following followers")
        for follower in tweepy.Cursor(self.api.followers).items():
            if not follower.following:
                self.logger.info(f"Following {follower.name}")
                try:
                    follower.follow()
                except Exception as e:
                    self.logger.error('An error occurred when try to follow back new follower: %s', e, exc_info=1)
