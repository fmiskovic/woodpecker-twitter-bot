import logging
import os

import tweepy

logging.config.fileConfig('logging.config')
logger = logging.getLogger(__name__)


def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_KEY")
    access_token_secret = os.getenv("ACCESS_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Failed to authenticate and to create Twitter API", exc_info=True)
        raise e
    logger.info("Twitter API created")
    return api
