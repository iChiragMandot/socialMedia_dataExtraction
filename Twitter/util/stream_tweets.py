# INPUT: search terms(multiple search terms can be given)
# OUPUT: Tweets with metadata
# This function will return real time tweets related to the search term

import json
import tweet_stream as tsr
import json
import twitter_acc_authorization as ta
from au import flags,au

flags.DEFINE_string('stream_term','None','Enter the term or a series of comma separated terms to get the results')
flags.DEFINE_output('streamed_tweets',None,'real time streamed tweets in JSON format')
flags.DEFINE_output('output_dir','','the output dir') 

def main(args):
     streamed_tweets=tsr.tweet_stream(ta.authorize(),au.FLAGS['stream_term'])
     with open(au.OUTPUT['streamed_tweets'],'w') as fh:
        json.dump(streamed_tweets,fh,indent=1)

if __name__=="__main__":
    au.run(main)
