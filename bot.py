import logging.config
import random
import time

from news import news_grabber, news_api_auth
from twitter import followers, tweets, twitter_api_auth

LONG_INTERVAL = 60 * 60  # sleep time interval is 60 minutes
SHORT_INTERVAL = 60 * 2  # sleep time interval is 2 minutes

logging.config.fileConfig('logging.config')
logger = logging.getLogger('bot')

news_api = news_api_auth.create_api()
news_grabber = news_grabber.NewsGrabber(news_api)

tw_api = twitter_api_auth.create_api()
tw_handler = tweets.TweetsHandler(tw_api)
followers_handler = followers.FollowersHandler(tw_api)


def get_news(query=None, category=None, country=None, language='en'):
    return news_grabber.get_news(query=query, category=category, country=country, language=language)


def tweet_news(news_item, hash_tag=None):
    return tw_handler.post_new_tweet(text=news_item.description, source=news_item.url, hashtag=hash_tag)


keywords = ['cryptocurrency', 'ethereum', 'bitcoin', 'XRP', 'litecoin']

while True:
    # follow new followers
    # followers_handler.follow_followers()

    # choose random keyword
    keyword = random.choice(keywords)

    news = get_news(query=keyword, language='en')
    if len(news) == 0:
        # if there are no news, take a short break
        logger.info(f'I did not find any news for keyword %s', keyword)
        logger.info(f'Taking a %s minutes break...', SHORT_INTERVAL / 60)
        time.sleep(SHORT_INTERVAL)
    else:
        logger.info('Tweet attempt about ' + keyword)
        hashtag = '#cryptocurrencynews #' + keyword
        for n in news:
            result = tweet_news(news_item=n, hash_tag=hashtag)
            if result is not None:
                logging.info(f'Taking a %s minutes break...', LONG_INTERVAL / 60)
                time.sleep(LONG_INTERVAL)
                logger.info('OK I am ready to continue. Lets tweet something again...')
