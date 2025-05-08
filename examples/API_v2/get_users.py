import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# Get Users

# This endpoint/method returns a variety of information about one or more users
# specified by the requested IDs or usernames

user_ids = [1438365197505232902, 1859490326316187649]

# By default, only the ID, name, and username fields of each user will be
# returned
# Additional fields can be retrieved using the user_fields parameter
response = client.get_users(ids=user_ids, user_fields=["profile_image_url"])

for user in response.data:
    print(user.username, user.profile_image_url)
