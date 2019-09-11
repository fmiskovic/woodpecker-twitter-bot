import logging.config
import time

from news import news_grabber, news_api_auth
from twitter import followers, tweets, twitter_api_auth

SLEEP_TIME = 60 * 60  # sleep time interval is 60 minutes

keywords = ['cryptocurrency', 'ethereum', 'bitcoin', 'XRP', 'litecoin', 'blockchain']

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


def collect_news():
    top_news = []
    for keyword in keywords:
        k_news = get_news(query=keyword, language='en')
        if len(k_news) > 0:
            logger.info(f'Found %d news for keyword %s', len(k_news), keyword)
            top_news = top_news + k_news
        else:
            logger.info(f'I did not find any news for keyword %s', keyword)
    return top_news


while True:
    # follow new followers
    # followers_handler.follow_followers()

    news = collect_news()
    if len(news) == 0:
        logger.info('There are no news at the moment')

    for n in news:
        hashtag = '#cryptocurrencynews #' + n.query
        logger.info('Tweet attempt about ' + n.query)
        result = tweet_news(news_item=n, hash_tag=hashtag)
        if result is not None:
            logging.info(f'Taking a %s minutes break...', SLEEP_TIME / 60)
            time.sleep(SLEEP_TIME)
            logger.info('OK I am ready to continue. Lets tweet something again...')

    logger.info(f'Taking a %s minutes break...', SLEEP_TIME / 60)
    time.sleep(SLEEP_TIME)
    logger.info('OK I am ready to continue. Lets tweet something again...')
