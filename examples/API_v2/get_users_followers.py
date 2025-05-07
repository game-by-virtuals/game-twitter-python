import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# Get User's Followers

# This endpoint/method returns a list of users who are followers of the
# specified user ID

user_id = 1859490326316187649

# By default, only the ID, name, and username fields of each user will be
# returned
# Additional fields can be retrieved using the user_fields parameter
response = client.get_users_followers(
    user_id, user_fields=["profile_image_url"]
)

if response.data:
    for user in response.data:
        print(user.username, user.profile_image_url)

# By default, this endpoint/method returns 100 results
# You can retrieve up to 1000 users by specifying max_results
response = client.get_users_followers(user_id, max_results=1000)
