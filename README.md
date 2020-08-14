# woodpecker-twitter-bot

###GENERAL

This is a Twitter bot showcase designed to post news periodically on Twitter and it's example can be found here:
https://twitter.com/crypto_topics

This showcase uses https://newsapi.org API to download specific news.

###PRE-CONDITION
Install python3.7.* and Pip

###BOT INSTALLATION
`git clone https://github.com/fmiskovic/woodpecker-twitter-bot.git`

`pip3 install -r requirements.txt`
###BOT CONFIGURATION
Register at https://developer.twitter.com/ and https://newsapi.org/ and generate keys and access tokens 
which must be added to the following environment variables:

#####[NEWSAPI]:
`NEWS_API_KEY`

#####[TWITTER]: 
`CONSUMER_KEY`

`CONSUMER_SECRET`

`ACCESS_KEY`

`ACCESS_SECRET`

#####[BOT] (this is optional, if not specified, check config.ini file to see default values):
`BOT_SLEEP_TIME` - specifies how for long the bot will be inactive in seconds

`BOT_COUNTRY` - specifies country of the news source

`BOT_CATEGORY` - specifies category of the news source

`BOT_LANGUAGE` - specifies language of the news source, for example: 'bitcoin'

`BOT_HASHTAG` - specifies which hashtags to add in a twitter post

`BOT_QUERIES` - specifies key words for searching the news at https://newsapi.org, for example: 'bitcoin'

`BOT_BLACKLISTED_SOURCES` - specifies blacklist news sources that you don't want to consume