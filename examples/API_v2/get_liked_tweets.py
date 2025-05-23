import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# Get User's Liked Tweets

# This endpoint/method allows you to get information about a user’s liked 
# Tweets

user_id = client.get_me().data['id']

# By default, only the ID and text fields of each Tweet will be returned
# Additional fields can be retrieved using the tweet_fields parameter
response = client.get_liked_tweets(user_id, user_auth=True, tweet_fields=["created_at"])

if response.data:
    for tweet in response.data:
        print(tweet.id, tweet.created_at)
