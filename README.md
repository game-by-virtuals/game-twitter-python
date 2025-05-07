# Virtuals Protocol Tweepy: Twitter for Python!

## Installation

The easiest way to install the latest version from PyPI is by using
[pip](https://pip.pypa.io/):

```bash
pip install virtuals-tweepy
```

## Quickstart: Initialize Client with Virtuals Protocol's GAME Access Token

### How to Get a GAME API Key
1. Go to the Virtuals Protocol's [GAME Console](https://console.game.virtuals.io/)
2. Sign in with your wallet.
3. Click on "**Create a New Project**" to register a new project.
4. Once your project is created, click on "**Generate one now**" under "API Key" to generate your API key.

### How to Get GAME X Access Token (Virtuals Protocol's X Enterprise API)

To get the access token for this option, run the following command:

```bash
poetry run virtuals-tweepy auth -k <GAME_API_KEY>
```

You will see the following output:

```bash
Waiting for authentication...

Visit the following URL to authenticate:
https://x.com/i/oauth2/authorize?response_type=code&client_id=VVdyZ0t4WFFRMjBlMzVaczZyMzU6MTpjaQ&redirect_uri=http%3A%2F%2Flocalhost%3A8714%2Fcallback&state=866c82c0-e3f6-444e-a2de-e58bcc95f08b&code_challenge=K47t-0Mcl8B99ufyqmwJYZFB56fiXiZf7f3euQ4H2_0&code_challenge_method=s256&scope=tweet.read%20tweet.write%20users.read%20offline.access
```

After authenticating, you will receive the following message:

```bash
Authenticated! Here's your access token:
apx-<xxx>
```

With this access token, you can enjoy up to 35 calls per 5 minutes to the X API, which is significantly higher than the standard X API plan.

If you've obtained a `game_twitter_access_token` via the GAME authentication flow, you can now initialize the Tweepy client directly with it:

```python
from virtuals_tweepy import Client

game_twitter_access_token = "apx-<game-twitter-access-token>"

client = Client(
    game_twitter_access_token=game_twitter_access_token
)
```

### Using your own X API credentials

- If you don't already have one, create a X (twitter) account and navigate to the [developer portal](https://developer.x.com/en/portal/dashboard).
- Create a project app, generate the following credentials and set them as environment variables (e.g. using a `.bashrc` or a `.zshrc` file):
  - `TWITTER_BEARER_TOKEN`
  - `TWITTER_API_KEY`
  - `TWITTER_API_SECRET_KEY`
  - `TWITTER_ACCESS_TOKEN`
  - `TWITTER_ACCESS_TOKEN_SECRET`

If you decide to use your own X API credentials, you can initialize the Tweepy client with them as follows:

```python
from virtuals_tweepy import Client

consumer_key = "<twitter-api-key>"
consumer_secret = "<twitter-api-secret-key>"
access_token = "<twitter-access-token>"
access_token_secret = "<twitter-access-token-secret>"

client = Client(
  consumer_key=consumer_key,
  consumer_secret=consumer_secret,
  access_token=access_token,
  access_token_secret=access_token_secret,
)
```

Latest version of Python and older versions not end of life (bugfix and security) are supported.

## Acknowledgments

This project is a modified version of [Tweepy](https://github.com/tweepy/tweepy) by [Virtuals Protocol](https://virtuals.io/), originally created by Joshua Roesslein.
Original work is Copyright (c) 2009-2023 Joshua Roesslein and is licensed under the MIT License.
