import logging.config
import time

from config.bot_config import BotConfig
from news import news_grabber, news_api_auth
from twitter import followers, tweets, twitter_api_auth

# Initialize and configure logger
logging.config.fileConfig('logging.config')
logger = logging.getLogger('bot')

# Initialize news api
news_api = news_api_auth.create_api()
news_grabber = news_grabber.NewsGrabber(news_api)

# Initialize twitter api
tw_api = twitter_api_auth.create_api()
tw_handler = tweets.TweetsHandler(tw_api)
followers_handler = followers.FollowersHandler(tw_api)

# Initialize constants
bot_config = BotConfig()
bot_config.initialize()
SLEEP_TIME = bot_config.get_property_value('BOT_SLEEP_TIME')
COUNTRY = bot_config.get_property_value('BOT_COUNTRY')
CATEGORY = bot_config.get_property_value('BOT_CATEGORY')
LANGUAGE = bot_config.get_property_value('BOT_LANGUAGE')
HASHTAG = bot_config.get_property_value('BOT_HASHTAG')
KEYWORDS = bot_config.get_property_values('BOT_QUERIES')


def get_news(query=None, category=None, country=None, language='en'):
    return news_grabber.get_news(query=query, category=category, country=country, language=language)


def tweet_news(news_item, hash_tag=None):
    return tw_handler.post_new_tweet(text=news_item.description, source=news_item.url, hashtag=hash_tag)


def collect_news():
    top_news = []
    if len(KEYWORDS) == 0:
        return get_news(country=COUNTRY, category=CATEGORY, language=LANGUAGE)

    for keyword in KEYWORDS:
        k_news = get_news(query=keyword, language=LANGUAGE)
        if len(k_news) > 0:
            logger.info(f'Found %d news for keyword %s', len(k_news), keyword)
            top_news = top_news + k_news
        else:
            logger.info(f'I did not find any news for keyword %s', keyword)
    return top_news


def sleep():
    logging.info(f'Taking a %s minutes break...', SLEEP_TIME / 60)
    time.sleep(SLEEP_TIME)
    logger.info('OK I am ready to continue. Lets tweet something again...')


def main():
    while True:
        # follow new followers
        # followers_handler.follow_followers()

        news = collect_news()
        if len(news) == 0:
            logger.info('There are no news at the moment')

        for n in news:
            hash_tag = '#' + HASHTAG + ' #' + n.query
            logger.info('Tweet attempt about ' + n.query)
            result = tweet_news(news_item=n, hash_tag=hash_tag)
            if result is not None:
                sleep()
        sleep()


if __name__ == '__main__':
    main()
