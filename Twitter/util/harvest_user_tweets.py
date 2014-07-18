# INPUT: Screen Name or User Id of the user
# OUTPUT: All the tweets of a user with some limitations. Refer the lib function get_user_tweet for it

from au import flags,au
import json
import twitter
import get_user_tweets as ut
import twitter_acc_authorization as ta

flags.DEFINE_string('ID',None,'Either Screen Name or User ID')
flags.DEFINE_output('user_tweets',None,'All the user tweets')
flags.DEFINE_output('output_dir','','The output dir') 

def main(args):
    full_user_tweets=ut.get_user_tweets(ta.authorize(),au.FLAGS['ID'])
    with open(au.OUTPUT['user_tweets'],'w') as fh:
        json.dump(full_user_tweets,fh,indent=1)
       

if __name__=="__main__":
    au.run(main)
