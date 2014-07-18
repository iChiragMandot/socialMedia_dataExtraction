'''
This wrapper function will handle various HTTP errors like rate limits(429 error) or 'fail whale'(503 error)
'''

import sys
import time
from urllib2 import URLError
from httplib import BadStatusLine
import json
import twitter

def make_twitter_request(twitter_api,twitter_api_func,max_errors=10,*args,**kw):
# A nested helper function that handles common HTTPErrors. Return an updated value for wait period if the problem
# is a 500 level error. Block until the rate limit is rser if its a rate limiting issue(429 error). 
#Returns None for 401 and 404 errors, which requires special handling by the caller.
    def handle_twitter_http_error(e,wait_period=2,sleep_when_rate_limted=True):
        if wait_period>3600: # seconds
            print >> sys.stderr,'Too many retries.Quitting.'
            raise e
        if e.e.code==401:
            print >> sys.stderr,'Encountered 401 Error (Not authorized)'
            return None
        elif e.e.code==404:
            print >> sys.stderr,'Encountered 404 Error(Not found)'
        elif e.e.code==429:
            print sys.stderr,'Encountered 429 error(Rate limit exceeded)'
            if sleep_when_rate_limited:
                print >> sys.stderr,"Retrying in 15 minutes..."
                sys.stderr.flush()
                time.sleep(60*15+5)
                print >> sys.stderr,'....Awake now and trying again'
                return 2
            else:
                raise e
        elif e.e.code in (500,502,503,504):
            print >> sys.stderr,'Encountered %i Error. retrying in %i seconds' % (e.e.code,wait_period)
            time.sleep(wait_period)
            return wait_period
        else:
            raise e
    wait_period=2
    error_count=0
    while True:
            try:
                return twitter_api_func(*args,**kw)
            except twitter_api.TwitterHTTPError,e:
                error_count=0
                wait_period=handle_twitter_http_error(e,wait_period)
                if wait_period is None:
                    return
            except URLError,e:
                error_count+=1
                print >> sys.stderr,"URLError encountered.Continuing"
                if error_count>max_errors:
                    print >> sys.stderr,"Too many consecutive errors..bailing out"
                    raise
            except BadStatusLine,e:
                error_count=1
                print >> sys.stderr,"BadStatusLine encountered.Continuing"
                if error_count>max_errors:
                    print >> sys.stderr,"Too many consecutive errors/..bailing out"
                    raise


