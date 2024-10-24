"""
DS4300: Large-Scale Information Storage and Retrieval
Homework 1: Twitter Engineering
Urvi Bhojani, Rishita Shroff
January 19th, 2023

Twitter Engineering Database API for MySQL
"""

class Tweets:

    def __init__(self, tweet_id, user_id, tweet_ts, tweet_text):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.tweet_ts = tweet_ts
        self.tweet_text = tweet_text

class Follow:

    def __init__(self, user_id, follows_id):
        self.user_id = user_id
        self.follows_id = follows_id

def __str__(self):
    return f"Follow: {self.user_id} ({self.follows_id})"
