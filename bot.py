import logging.config
import time

from news import news_grabber, news_api_auth
from twitter import followers, tweets, twitter_api_auth

INTERVAL = 60 * 60  # sleep time interval is 5 minutes

logging.config.fileConfig('logging.config')
logger = logging.getLogger('bot')

news_api = news_api_auth.create_api()
news_grabber = news_grabber.NewsGrabber(news_api)

tw_api = twitter_api_auth.create_api()
tw_handler = tweets.TweetsHandler(tw_api)
followers_handler = followers.FollowersHandler(tw_api)


def tweet_something_about(keyword):
    news = news_grabber.get_news(keyword, category='business')
    if len(news) == 0:
        logger.info(f'There are no news about %s at the moment', keyword)
        return

    logger.info('Tweeting about ' + keyword)

    for n in news:
        tw_handler.post_new_tweet(n.description, n.url)
        logging.info(f'Taking a %d minutes break...', INTERVAL)
        time.sleep(INTERVAL)
        logger.info('OK I am ready to continue. Lets tweet something...')


while True:
    # follow new followers
    followers_handler.follow_followers()

    # check for cryptocurrency news and tweet about it
    tweet_something_about('cryptocurrency')
