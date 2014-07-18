# This will take tweets as input and return the text of the tweets
#The input will be either results obtained from search or stream functions
def get_tweetText(tweet_blob):
    tweet_text=json.dumps([tweet['text'] for tweet in tweet_blob],indent=1)
    return tweet_text
    
