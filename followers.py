import logging

import tweepy

logging.config.fileConfig('logging.config')
logger = logging.getLogger(__name__)


class FollowersHandler:

    def __init__(self, tw_api):
        logger.info('Initializing FollowersHandler')
        self.api = tw_api
        self.me = self.api.me()

    def follow_followers(self):
        logger.info("Retrieving and following followers")
        for follower in tweepy.Cursor(self.api.followers).items():
            if not follower.following:
                logger.info(f"Following {follower.name}")
                follower.follow()
