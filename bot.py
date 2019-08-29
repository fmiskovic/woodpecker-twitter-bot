import logging.config
import time

from src.news import news_api_auth
from src.news import news_grabber
from src.twitter import followers
from src.twitter import tweets
from src.twitter import twitter_api_auth

INTERVAL = 60 * 60 * 6  # tweet every 6 hours

logging.config.fileConfig('logging.config')
logger = logging.getLogger(__name__)

news_api = news_api_auth.create_api()
news_grabber = news_grabber.NewsGrabber(news_api)

tw_api = twitter_api_auth.create_api()
tw_handler = tweets.TweetsHandler(tw_api)
followers_handler = followers.FollowersHandler(tw_api)


def tweet_something_about(keyword):
    news = news_grabber.get_news(keyword)
    if len(news) == 0:
        return
    logger.info('Tweeting about ' + keyword)
    for n in news:
        tw_handler.post_new_tweet(n.title, n.url)


while True:
    # follow new followers
    followers_handler.follow_followers()

    # check for bitcoin news and tweet about it
    tweet_something_about('bitcoin')

    # check for cryptocurrency news and tweet about it
    tweet_something_about('cryptocurrency')

    # check for litecoin news and tweet about it
    tweet_something_about('litecoin')

    # check for ethereum news and tweet about it
    tweet_something_about('ethereum')

    logger.info('going to sleep now...')
    time.sleep(INTERVAL)
