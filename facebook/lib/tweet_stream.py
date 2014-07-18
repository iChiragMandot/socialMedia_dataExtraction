# The StreamingAPI will give teh realtime tweet as opposed to searchAPI which might give a little bit historical result

import twitter
import sys

def tweet_stream(twitter_api,q):
    print >> sys.stderr, 'Filtering the public timeline for track="%s"' % (q,)
    twitter_stream=twitter.TwitterStream(auth=twitter_api.auth)
    stream=twitter_stream.statuses.filter(track=q)
    for tweet in stream:
        output_tweet=tweet['text']
        print output_tweet

    return output_tweet
