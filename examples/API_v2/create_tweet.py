import os

from virtuals_tweepy import Client
from dotenv import load_dotenv

load_dotenv()

game_twitter_access_token = os.environ.get("GAME_TWITTER_ACCESS_TOKEN")

client = Client(game_twitter_access_token = game_twitter_access_token)

# Create Tweet

# The app and the corresponding credentials must have the Write permission

# Check the App permissions section of the Settings tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps

# Make sure to reauthorize your app / regenerate your access token and secret 
# after setting the Write permission

# Example 1: Create a regular Tweet
response = client.create_tweet(
    text="This Tweet was Tweeted using Virtuals Tweepy and Twitter API v2!"
)
print(f"https://twitter.com/user/status/{response.data['id']}")

# Example 2: Create a Tweet in a Community
# Note: The authenticated user must be a member of the Community
# response = client.create_tweet(
#     text="This Tweet was posted in a Community using Tweepy and Twitter API v2!",
#     community_id="INSERT_COMMUNITY_ID_HERE"
# )
# print(f"https://twitter.com/user/status/{response.data['id']}")
