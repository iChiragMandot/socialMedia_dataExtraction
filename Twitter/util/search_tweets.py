# Inputs: Search term
# Output: Tweets in JSON format with complete metadata

import twitter
import json
from au import flags,au
import twitter_searchTweets as ts
import twitter_acc_authorization as ta

flags.DEFINE_string('search_term',None,'Enter the keyword to search tweets')
flags.DEFINE_output('tweets_with_metadata',None,'The tweets will complete information about it is returned')
flags.DEFINE_output('output_dir','','The output dir')

def main(args):
    tweets_with_metadata= ts.search_tweets(ta.authorize(),au.FLAGS['search_term'])
    with open(au.OUTPUT['tweets_with_metadata'],'w') as fh: 
        json.dump(tweets_with_metadata,fh,indent=1)

if __name__=="__main__":
    au.run(main)
