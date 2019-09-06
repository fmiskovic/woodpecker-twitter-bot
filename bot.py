import logging.config
import time

from twitter import followers, tweets, twitter_api_auth
from news import news_grabber, news_api_auth

INTERVAL = 60 * 5  # sleep time interval is 5 minutes

logging.config.fileConfig('logging.config')
logger = logging.getLogger('bot')

news_api = news_api_auth.create_api()
news_grabber = news_grabber.NewsGrabber(news_api, logger)

tw_api = twitter_api_auth.create_api()
tw_handler = tweets.TweetsHandler(tw_api, logger)
followers_handler = followers.FollowersHandler(tw_api, logger)


def tweet_something_about(keyword):
    news = news_grabber.get_news(keyword)
    if len(news) == 0:
        return False
    logger.info('Tweeting about ' + keyword)
    # tw_handler.post_new_tweet(news[0].title, news[0].url)
    for n in news:
        tw_handler.post_new_tweet(n.description, n.url)
        logging.info('Taking a nap break...')
        time.sleep(INTERVAL)
        logger.info('OK I am ready to continue. Lets tweet something')


while True:
    # follow new followers
    followers_handler.follow_followers()

    # check for bitcoin news and tweet about it
    tweet_something_about('bitcoin')

    # check for cryptocurrency news and tweet about it
    tweet_something_about('cryptocurrency')
