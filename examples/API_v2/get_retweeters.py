import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# Get Tweet's Retweeters

# This endpoint/method allows you to get information about who has Retweeted a
# Tweet

tweet_id = 1460323737035677698

# By default, only the ID, name, and username fields of each user will be
# returned
# Additional fields can be retrieved using the user_fields parameter
response = client.get_retweeters(tweet_id, user_fields=["profile_image_url"])
print(response)

if response.data:
    for user in response.data:
        print(user.username, user.profile_image_url)
