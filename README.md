# Virtual Tweepy: Twitter for Python!

## Installation

The easiest way to install the latest version from PyPI is by using
[pip](https://pip.pypa.io/):

    pip install virtuals-tweepy

Using GAME's X enterprise API credentials (higher rate limits)

- To get the access token for this option, run the following command:

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

Using your own X API credentials

- If you don't already have one, create a X (twitter) account and navigate to the [developer portal](https://developer.x.com/en/portal/dashboard).
- Create a project app, generate the following credentials and set them as environment variables (e.g. using a `.bashrc` or a `.zshrc` file):
  - `TWITTER_BEARER_TOKEN`
  - `TWITTER_API_KEY`
  - `TWITTER_API_SECRET_KEY`
  - `TWITTER_ACCESS_TOKEN`
  - `TWITTER_ACCESS_TOKEN_SECRET`

Latest version of Python and older versions not end of life (bugfix and security) are supported.

## Acknowledgments

This project is a modified version of [Tweepy](https://github.com/tweepy/tweepy), originally created by Joshua Roesslein.
Original work is Copyright (c) 2009-2023 Joshua Roesslein and is licensed under the MIT License.
