import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# You can specify expansions to retrieve additional objects that relate to the
# returned results
response = client.search_recent_tweets(
    "Tweepy", expansions=["attachments.media_keys", "author_id"]
)
tweets = response.data

# You can then access those objects in the includes Response field
includes = response.includes
users = includes["users"]

# The IDs that represent the expanded objects are included directly in the
# returned data objects
for tweet in tweets:
    print(tweet.author_id)

# An efficient way of matching expanded objects to each data object is to
# create a dictionary of each type of expanded object, with IDs as keys
users = {user["id"]: user for user in users}
for tweet in tweets:
    print(tweet.id, users[tweet.author_id].username)
