import logging.config
import os

from newsapi import newsapi_client

logging.config.fileConfig('logging.config')
logger = logging.getLogger(__name__)


def create_api():
    """authenticate to newsapi.org and get NewsApiClient"""
    logger.info('creating News API client...')
    return newsapi_client.NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
