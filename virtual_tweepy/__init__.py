# Tweepy
# Copyright 2009-2023 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '4.15.0'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from virtual_tweepy.api import API
from virtual_tweepy.auth import (
    AppAuthHandler, OAuthHandler, OAuth1UserHandler, OAuth2AppHandler,
    OAuth2BearerHandler, OAuth2UserHandler
)
from virtual_tweepy.cache import Cache, FileCache, MemoryCache
from virtual_tweepy.client import Client, Response
from virtual_tweepy.cursor import Cursor
from virtual_tweepy.direct_message_event import (
    DirectMessageEvent, DIRECT_MESSAGE_EVENT_FIELDS, DM_EVENT_FIELDS
)
from virtual_tweepy.errors import (
    BadRequest, Forbidden, HTTPException, NotFound, TooManyRequests,
    TweepyException, TwitterServerError, Unauthorized
)
from virtual_tweepy.list import List, LIST_FIELDS
from virtual_tweepy.media import Media, MEDIA_FIELDS
from virtual_tweepy.pagination import Paginator
from virtual_tweepy.place import Place, PLACE_FIELDS
from virtual_tweepy.poll import Poll, POLL_FIELDS
from virtual_tweepy.space import PUBLIC_SPACE_FIELDS, Space, SPACE_FIELDS
from virtual_tweepy.streaming import (
    StreamingClient, StreamResponse, StreamRule
)
from virtual_tweepy.tweet import (
    PUBLIC_TWEET_FIELDS, ReferencedTweet, Tweet, TWEET_FIELDS
)
from virtual_tweepy.user import User, USER_FIELDS

# Global, unauthenticated instance of API
api = API()
