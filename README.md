# woodpecker-twitter-bot

### GENERAL

This Twitter bot is designed to consume specific top-headlines from https://newsapi.org and to post it periodically on Twitter.
The bot itself is vary configurable. Parameters like posting time period, language of the post, topic etc, can be configured via environment variables which I am describing bellow.

The showcase example can be found here:
https://twitter.com/crypto_topics

### PRE-CONDITION
I recomend you to setup and install this bot in [Heroku](https://heroku.com/) like I did, but of course you can do it on Google Cloud or AWS.
In case you want to test it or just run it localy or in your personal evironment, [python3.7.*](https://realpython.com/installing-python/) and [PIP](https://pip.pypa.io/en/stable/installing/) must be installed.

### BOT INSTALLATION

`git clone https://github.com/fmiskovic/woodpecker-twitter-bot.git` or download this repository.

`pip3 install -r requirements.txt`

### BOT CONFIGURATION
First you need to register at [Twitter Developer](https://developer.twitter.com/) and [News API](https://newsapi.org/) in order to generate keys and access tokens 
which must be added to the following environment variables:

##### [NEWSAPI]:

`NEWS_API_KEY`

##### [TWITTER]: 

`CONSUMER_KEY`

`CONSUMER_SECRET`

`ACCESS_KEY`

`ACCESS_SECRET`

##### [BOT] (this is optional, if not specified, check config.ini file to see default values):

`BOT_SLEEP_TIME` - specifies how for long the bot will be inactive in seconds

`BOT_COUNTRY` - specifies country of the news source

`BOT_CATEGORY` - specifies category of the news source

`BOT_LANGUAGE` - specifies language of the news source, for example: 'bitcoin'

`BOT_HASHTAG` - specifies which hashtags to add in a twitter post

`BOT_QUERIES` - specifies key words for searching the news at https://newsapi.org, for example: 'bitcoin'

`BOT_BLACKLISTED_SOURCES` - specifies blacklist news sources that you don't want to consume

### RUNNING THE BOT

Open terminal and run:

`python3 bot.py`

That is it. If you need my support, do not hesitate to contact me via email fmiskovic@yandex.com.

If you like this idea, consider becoming a patreon:
https://www.patreon.com/filthygoat

Thank you for supporting!
