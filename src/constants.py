from dotenv import load_dotenv

import os

USERNAME = "cursedkidd"

# TWEET_USER_CONTAINER = "//span[@data-testid='User-Names']"
# TWEET_USERNAME_TEXT = f'{TWEET_USER_CONTAINER}/div[2]/div/div[1]/a/div/span[text()=@{USERNAME}]'
# TWEET_CONTENT_CONTAINER = "//div[@data-testid='tweetText']"
# TWEET_CONTENT_TEXT = f'{TWEET_CONTENT_CONTAINER}/span'
TWEET_CONTAINER = "//article[@data-testid='tweet']"

load_dotenv()

TWITTER_LOGIN_EMAIL = os.getenv('TWITTER_LOGIN_EMAIL')
TWITTER_LOGIN_USERNAME = os.getenv('TWITTER_LOGIN_USERNAME')
TWITTER_LOGIN_PASSWORD = os.getenv('TWITTER_LOGIN_PASSWORD')

DATA_DIR = "./data"
