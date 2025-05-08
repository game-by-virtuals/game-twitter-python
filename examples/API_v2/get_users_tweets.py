import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# Get User's Tweets

# This endpoint/method returns Tweets composed by a single user, specified by
# the requested user ID

user_id = 1859490326316187649

response = client.get_users_tweets(user_id)

# By default, only the ID and text fields of each Tweet will be returned
if response.data:
    for tweet in response.data:
        print(tweet.id)
        print(tweet.text)

# By default, the 10 most recent Tweets will be returned
# You can retrieve up to 100 Tweets by specifying max_results
response = client.get_users_tweets(user_id, max_results=100)
