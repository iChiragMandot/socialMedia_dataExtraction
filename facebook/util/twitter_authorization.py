# This function will authorize the user using the KEYS
import twitter
import json
from au import au,flags
import twitter_acc_authorization as ta

#au.flags.DEFINE_string('CONSUMER_KEY','','Consumer Key')
#au.flags.DEFINE_string('CONSUMER_SECRET','','Consumer Secret')
#au.flags.DEFINE_string('OAUTH_TOKEN','','Authorization Token')
#au.flags.DEFINE_string('OAUTH_TOKEN_SECRET','','Auth Secret')
au.flags.DEFINE_output('twitter_api','Authorized Token',{}, 'twitter_api_token.pyc')
au.flags.DEFINE_string('output_dir', '', 'the output dir')

def main(args):
#The following keys uses OAuth 2.0 authorization and are generated from Twitter account"""
#    CONSUMER_KEY='ccKltYEXKE8aRhM7q8xEwKwJq'
#    CONSUMER_SECRET='kurDCQPiktO3XFUpyIccr5bAXHJG3RgqCy6wkWh21Q7ncWw0zC'
#    OAUTH_TOKEN='176085284-fLUVqOFcrPyTmOycpKIhKhMoMj5llOHb8KrfKUQN'
#    OAUTH_TOKEN_SECRET='7z4nIomNUciLeZxmosUAgGMY0QovjNPVckv6pabHVAUEG'
    authorized_token={}
    authorized_token=ta.authorize()
#authorized_token=ta.authorize(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET) 
#authorized_token=ta.authorize(au.FLAGS['OAUTH_TOKEN'],au.FLAGS['OAUTH_TOKEN_SECRET'],au.FLAGS['CONSUMER_KEY'],au.FLAGS['CONSUMER_SECRET'])



if "__main__"==__name__:
    au.run(main)
