# It will take the tweet blob and return the mention of users if any
#Input from search or stream results
def userMention(tweet_blob):
    userMention=json.dumps([user_mention['screen_name'] \
            for tweet in tweet_blob  \
            for user_mention in tweet['entities']['user_mentions']],indent=1)
    return userMention
