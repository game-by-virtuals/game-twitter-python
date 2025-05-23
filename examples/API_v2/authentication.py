import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# GAME Twitter Access Token
game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

# You can authenticate as your app with just your GAME Twitter access token
client = Client(game_twitter_access_token=game_twitter_access_token)
print(f"Authenticated as user @{client.get_me().data['username']} with GAME Twitter access token")

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
print(f"Authenticated as user @{client.get_me().data['username']} with OAuth1.0a")

# You can authenticate as your app with just your bearer token
client = Client(bearer_token=bearer_token)
print(f"Authenticated as user @{client.get_me().data['username']} with OAuth2")
