import logging.config
import random
import time

from news import news_grabber, news_api_auth
from twitter import followers, tweets, twitter_api_auth

INTERVAL = 60 * 60  # sleep time interval is 60 minutes

logging.config.fileConfig('logging.config')
logger = logging.getLogger('bot')

news_api = news_api_auth.create_api()
news_grabber = news_grabber.NewsGrabber(news_api)

tw_api = twitter_api_auth.create_api()
tw_handler = tweets.TweetsHandler(tw_api)
followers_handler = followers.FollowersHandler(tw_api)


def get_news(query=None, category=None, country=None, language='en'):
    return news_grabber.get_news(query=query, category=category, country=country, language=language)


def tweet_news(news_items, hash_tag=None):
    for n in news_items:
        result = tw_handler.post_new_tweet(text=n.description, source=n.url, hashtag=hash_tag)
        if result is not None:
            logging.info(f'Taking a %s minutes break...', INTERVAL / 60)
            time.sleep(INTERVAL)
            logger.info('OK I am ready to continue. Lets tweet something again...')


keywords = ['cryptocurrency', 'ethereum', 'bitcoin', 'XRP', 'litecoin']

while True:
    # follow new followers
    # followers_handler.follow_followers()

    keyword = random.choice(keywords)
    news = get_news(query=keyword, language='en')
    if len(news) > 0:
        logger.info('Tweet attempt about ' + keyword)
        tweet_news(news_items=news, hash_tag='#cryptocurrencynews #' + keyword)
