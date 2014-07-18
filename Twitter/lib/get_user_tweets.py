'''
This function will return the tweets of a speicified user
Output Format: JSON, XML, RSS
Parameters:
user_id(optional)      : ID of the user for whom results are expected
screen_name            : Screen name of the user for whom results are expected
since_id(optional)     : Returns results with an ID greater than (that is, more recent than) the specified ID. 
                         There are limits to the number of Tweets which can be accessed through the API. 
                         If the limit of Tweets has occured since the since_id, 
                         the since_id will be forced to the oldest ID available.
count(optional)        : Specifies the number of tweets to try and retrieve, up to a maximum of 200. 
                         The value of count is best thought of as a limit to the number of tweets to return 
                         because suspended or deleted content is removed after the count has been applied. 
                         We include retweets in the count, even if include_rts is not supplied. 
                         It is recommended you always send include_rts=1 when using this API method.
max_id(optional)       : Returns results with an ID less than (that is, older than) or equal to the specified ID.
page(optional)         : Specifies the page of results to retrieve.//Soon will cease to be functional
trim_user(optional)    : When set to either true, t or 1, each tweet returned in a timeline will
                         include a user object including only the status authors numerical ID. 
                         Omit this parameter to receive the complete user object.
include_rts(optional)  : When set to either true, t or 1,the timeline will contain 
                         native retweets (if they exist) in addition to the standard stream of tweets.
exclude_replies(opt)   : This parameter will prevent replies from appearing in the returned timeline.
contributor_details(optional) : This parameter enhances the contributors element of 
                                the status response to include the screen_name of the contributor. 
                                By default only the user_id of the contributor is included.
For more details, visit: https://dev.twitter.com/docs/api/1/get/statuses/user_timeline

'''
import sys
import twitter
import json
import error_handler
def get_user_tweets(twitter_api,screen_name=None,user_id=None,max_results=1000):
    assert(screen_name!=None)!=(user_id!=None),"Must have screen_name or user_id, but noth both"
    kw= { # Keyword args for the Twitter API call
        'count':200,
        'trim_user':'true',
        'include_rts':'true',
        'since_id':1
        }
    if screen_name:#takes either the screen name or user id
        kw['screen_name']=screen_name
    else:
        kw['user_id']=user_id
    max_pages=16
    results=[]
    tweets=error_handler.make_twitter_request(twitter_api,twitter_api.statuses.user_timeline,**kw)# error handling incase the tweets are over or any other connection issue
    if tweets is None: # 401(Not Authorized)-Need to bail out on loop entry
        tweets=[]
    results+=tweets
    print >> sys.stderr,'Fetched %i tweets' % len(tweets)
    page_num=1 
# Many times we make extra requests then desired and vice versa. The following code will handle those issues
    if max_results==kw['count']:
        page_num=max_pages # prevent loop entry
    while page_num<max_pages and len(tweets)>0 and len(results)<max_results:
        # See https://dev.twitter.com/docs/working-with-timelines
            kw['max_id']=min([tweet['id'] for tweet in tweets])-1
            tweets=error_handler.make_twitter_request(twitter_api,twitter_api.statuses.user_timeline,**kw)
            results+=tweets
            print >> sys.stderr,'Fetched % i tweets' % (len(tweets))
            page_num+=1
    print >> sys.stderr, 'Done fetching tweets'
    return results[:max_results]
