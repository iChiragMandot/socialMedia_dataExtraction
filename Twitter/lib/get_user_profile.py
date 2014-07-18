'''
This function will return upto 100 users worth of extended information, specified by either ID, screen name or combination of two.
Output: JSON format
Parameters:
screen_name(optional):comma separated list of upto 100 users in a single request is permitted
user_id(optional):comma separated list of user IDs, upto 100 are allowed in a single request
include_entities(optional): True or False. Based on the input, it will load entities.
For more information on user/lookup, visit: https://dev.twitter.com/docs/api/1/get/users/lookup
For more information on entities, visit: https://dev.twitter.com/docs/entities
'''

import json
import twitter


def get_user_profile(twitter_api, screen_names=None, user_ids=None):
# It should have either screen name or user id and not both. The assert function will assure it.
    assert(screen_names!=None) !=(user_ids!=None), "Must have screen_name or user_id, but not both"
    user_data={}
    IDs=screen_names or user_ids
    while len(IDs)>0:
        IDs_str=','.join([str(item) for item in IDs[:100]]) # Formatting to make input an array of strings
        print "printing in get_user_profile"
        print IDs_str
        IDs=IDs[100:]
        if screen_names:
            response=twitter_api.users.lookup(screen_name=IDs_str) # fetches the user profile using screen name for all
            print response
        else:
            response=twitter_api.users.lookup(user_id=IDs_str)     # fetches the user profile using user id for all
            print response
        for user_info in response:
            if screen_names:
                user_data[user_info['screen_name']]=user_info      # Stores the user profile as per the ids provided
            else:
                user_data[user_info['id']]=user_info
    print user_data
    print "leaving the function"
    return user_data

