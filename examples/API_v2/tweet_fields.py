import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# You can specify additional Tweet fields to retrieve using tweet_fields
response = client.search_recent_tweets(
    "Virtuals Tweepy", tweet_fields=["created_at", "lang"]
)
tweets = response.data

# You can then access those fields as attributes of the Tweet objects
if tweets:
    for tweet in tweets:
        print(tweet.id, tweet.created_at)

    # Alternatively, you can also access fields as keys, like a dictionary
    for tweet in tweets:
        print(tweet["id"], tweet["lang"])

    # There’s also a data attribute/key that provides the entire data dictionary
    for tweet in tweets:
        print(tweet.data)
