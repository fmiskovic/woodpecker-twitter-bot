import tweepy


class FollowersHandler:

    def __init__(self, tw_api, logger):
        logger.info('Initializing FollowersHandler')
        self.api = tw_api
        self.me = self.api.me()
        self.logger = logger

    def follow_followers(self):
        self.logger.info("Retrieving and following followers")
        for follower in tweepy.Cursor(self.api.followers).items():
            if not follower.following:
                self.logger.info(f"Following {follower.name}")
                follower.follow()
