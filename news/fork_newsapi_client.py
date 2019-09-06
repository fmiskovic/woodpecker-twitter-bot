from sys import version_info

import requests
from requests.compat import basestring

from news import fork_const
from news.fork_newsapi_auth import NewsApiAuth
from news.fork_newsapi_exception import NewsAPIException


class NewsApiClient(object):

    def __init__(self, api_key):
        self.auth = NewsApiAuth(api_key=api_key)

    def get_top_headlines(self, q=None, sources=None, language='en', country=None, category=None, page_size=None,
                          page=None):

        # Define Payload
        payload = {}

        # Keyword/Phrase
        if q is not None:
            if is_valid_string(q):
                payload['q'] = q
            else:
                raise TypeError('keyword/phrase q param should be of type str')

        # Sources
        if (sources is not None) and ((country is not None) or (category is not None)):
            raise ValueError('cannot mix country/category param with sources param.')

        # Sources
        if sources is not None:
            if is_valid_string(sources):
                payload['sources'] = sources
            else:
                raise TypeError('sources param should be of type str')

        # Language
        if language is not None:
            if is_valid_string(language):
                if language in fork_const.languages:
                    payload['language'] = language
                else:
                    raise ValueError('invalid language')
            else:
                raise TypeError('language param should be of type str')

        # Country
        if country is not None:
            if is_valid_string(country):
                if country in fork_const.countries:
                    payload['country'] = country
                else:
                    raise ValueError('invalid country')
            else:
                raise TypeError('country param should be of type str')

        # Category
        if category is not None:
            if is_valid_string(category):
                if category in fork_const.categories:
                    payload['category'] = category
                else:
                    raise ValueError('invalid category')
            else:
                raise TypeError('category param should be of type str')

        # Page Size
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload['pageSize'] = page_size
                else:
                    raise ValueError('page_size param should be an int between 1 and 100')
            else:
                raise TypeError('page_size param should be an int')

        # Page
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload['page'] = page
                else:
                    raise ValueError('page param should be an int greater than 0')
            else:
                raise TypeError('page param should be an int')

        # Send Request
        r = requests.get(fork_const.TOP_HEADLINES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()


def is_valid_string(var):
    if version_info[0] == 3:
        return isinstance(var, str)
    elif version_info[0] == 2:
        return isinstance(var, basestring)
    else:
        raise SystemError("unsupported version of python detected (supported versions: 2, 3)")
