import twitter

def authorize():
# Default values of the keys are given as they will not change. Incase we want to use any other account, changes in keys need to be done here
    CONSUMER_KEY='ccKltYEXKE8aRhM7q8xEwKwJq'
    CONSUMER_SECRET='kurDCQPiktO3XFUpyIccr5bAXHJG3RgqCy6wkWh21Q7ncWw0zC'
    OAUTH_TOKEN='176085284-fLUVqOFcrPyTmOycpKIhKhMoMj5llOHb8KrfKUQN'
    OAUTH_TOKEN_SECRET='7z4nIomNUciLeZxmosUAgGMY0QovjNPVckv6pabHVAUEG'
    auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    twitter_api=twitter.Twitter(auth=auth)
    return twitter_api
