import logging.config

from news.news_model import News


class NewsGrabber:
    """Use this class to grab latest breaking news"""

    def __init__(self, news_api):
        """Init news api client"""
        self.news_api = news_api

        self.logger = logging.getLogger(__name__)
        self.logger.info('Initialized NewsApiClient')

    def get_news(self, query, category=None, country=None):
        """get latest breaking news"""
        news = []
        response = self.news_api.get_top_headlines(query=query, category=category, country=country, language='en')
        if response['status'] == 'ok':
            self.logger.info('Querying news went ok')
            for article in response['articles']:
                news.append(News(article['author'], article['title'], article['description'], article['url'],
                                 article['publishedAt']))
        self.logger.info(f'Found {len(news)} news')
        return news
