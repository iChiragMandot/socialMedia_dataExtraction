'''
This function will return the trending topics in the specified region default being world
The request limit is 15/user and 15/app in the time window of 15 minutes
Output: JSON format
Parameters:
    id:Yahoo!Where On Earth ID-It gives the location id which is used to get trends
    exclude: It will remove the specified hashtags from the output
For further information please refer:https://dev.twitter.com/docs/api/1.1/get/trends/place
Note: Trends are delayed by 5 minutes
'''

import json
import twitter


def search_trends(twitter_api,WOE_ID):
#prefix ID with underscore for quer;y string parameterization.
#without the underscore, the twitter package appends the ID value to the url as a special keyword argument.
    trends_output=json.dumps(twitter_api.trends.place(_id=WOE_ID),indent=1)
# The above call initiates an HTTP call to GET https://api.twitter.com/1.1/trends/place.json?id=WOE_ID
    return trends_output
    
