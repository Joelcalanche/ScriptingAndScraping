from typing import Text
import tweepy


auth = tweepy.OAuthHandler('ROdckafjS7T8rxfpOQaqvIQig', '6Rmcz2LxWjMEm1dC2bn8h0VYoerd48csyZSD2BMIapPzUEda6H')
auth.set_access_token('1465380008562761735-gGb4uQyfSfyUQrk74guYGkMdDfmGub', '9jViJiOgQPyYjmcDU7ejurg5hFIGKSeRwNe0YeZWhwWW4')



api = tweepy.API(auth)

public_tweets = api.home_timeline()


for tweet in public_tweets:
    print(tweet.text)