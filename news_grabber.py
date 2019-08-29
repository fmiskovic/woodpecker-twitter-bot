import logging.config

from news_model import News

logging.config.fileConfig('logging.config')
logger = logging.getLogger(__name__)


class NewsGrabber:
    """Use this class to grab latest breaking news"""

    def __init__(self, news_api):
        """Init news api client"""
        logger.info('Initializing NewsApiClient...')
        self.news_api = news_api

    def get_news(self, query):
        """get latest breaking news"""
        news = []
        response = self.news_api.get_top_headlines(query)
        if response['status'] == 'ok':
            logger.info('Querying news went ok')
            for article in response['articles']:
                news.append(News(article['author'], article['title'], article['description'], article['url'],
                                 article['publishedAt']))
        logger.info(f'Found {len(news)} news')
        return news
