# It will take tweet blob as input and return the hashtags used
# The input tweets are the ones received either from searching or streaming

def hashtags(tweet_blob):
    hashtags=json.dumps([hashtag['text'] for tweet in tweet_blob \
    for hashtag in tweet['entities']['hashtags']],indent=1)
    return hashtags
