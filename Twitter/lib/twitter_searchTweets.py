'''
Search Tweets using Keyword
The data is rate limited i.e. 180 requests/user and 450/app in 15 minutes time window
Output: JSON format
Parameters:
q:Query. The format of the query is important for efficient results. 
    watching now               :containing both "watching" and "now". This is the default operator.
    "happy hour"               :containing the exact phrase "happy hour".
    love OR hate               :containing either "love" or "hate" (or both).
    beer -root                 :containing "beer" but not "root".
    #haiku                     :containing the hashtag "haiku".
    from:alexiskold            :sent from person "alexiskold".
    to:techcrunch              :sent to person "techcrunch".
    @mashable                  :referencing person "mashable".
    superhero since:2010-12-27 :containing "superhero" and sent since date "2010-12-27" (year-month-day).
    ftw until:2010-12-27       :containing "ftw" and sent before the date "2010-12-27".
    movie -scary :)            :containing "movie", but not "scary", and with a positive attitude.
    flight :(                  : containing "flight" and with a negative attitude.
    traffic ?                  :containing "traffic" and asking a question.
    hilarious filter           :links:containing "hilarious" and linking to URL.
    news source:twitterfeed    : containing "news" and entered via TwitterFeed

geocode: The format will be "latitude,longtitude,radius". Ex. 37.3232,-122.232,1mi
lang:Ex. en,eu
locale: Specify the language of the query. Currently only `ja` is available
result_type: Ex. mixed,recent,popular. Default is mixed
count: Number of tweets per page. Max 100 is allowed, default is 15
until: returns tweet before the specified time. Format: YYYY-MM-DD
since_id:It will give the tweets from the ID given. Could be useful when the limit is reached
max_id:Returns the tweets with ID less than the given
include_entities:The entity node wont be included in case of false value.
callback:Returns the output in JSONP format. Not quite useful because of new authorization
For detailed explanation, please refer: https://dev.twitter.com/docs/api/1.1/get/search/tweets

'''
import twitter
import json

def search_tweets(twitter_api,q,count=100):
    search_results=twitter_api.search.tweets(q=q,count=count)
# Above call initiates an HTTP request to GET the search results
    tweet_blob=search_results['statuses']
    for _ in range(100):
        try:
            next_results=search_results['search_metadata']['next_results']
#As new tweets keep generating, we need to keep track of id of the last tweet and continue the search from there.
# The next_results gold the id
        except KeyError,e:
            print "no more search results :("
            break
        cursor=dict([new_param.split('=') for new_param in next_results[1:].split("&")])
# It creates a new paramters i.e cursor and pass them to fetch the next page of tweets 
        search_results=twitter_api.search.tweets(**cursor)
        tweet_blob+=search_results['statuses']
    output_tweets=json.dumps(tweet_blob,indent=1)
    return output_tweets
