import tweepy, os, pandas as pd, random as rd

# this part only to set and retrieve secrets in another file - omit when deployed

# import set_secrets
# set_secrets.set_secrets_env()
# print(os.environ["TWITTER_SNEMBOT_CKEY"])

# load data
txt = pd.read_csv("./texts.csv")

print(txt)

# select piece to tweet

twt = txt["text"][rd.randrange(0, len(txt["text"]))]
print(twt)

# authenticate
auth = tweepy.OAuthHandler(os.environ["TWITTER_SNEMBOT_CKEY"], os.environ["TWITTER_SNEMBOT_CSECRET"])
auth.set_access_token(os.environ["TWITTER_SNEMBOT_AKEY"], os.environ["TWITTER_SNEMBOT_ASECRET"])
api = tweepy.API(auth)

# tweet
api.update_status(twt)

