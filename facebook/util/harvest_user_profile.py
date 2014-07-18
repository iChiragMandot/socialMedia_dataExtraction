#INPUT: Screen name or User Id
#OUTPUT: Complete user profile i.e. followers, tweets etc


import get_user_profile as up
from au import au,flags
import twitter
import json
import twitter_acc_authorization as ta

flags.DEFINE_separatedlist('screen_name',None,'Enter screen name')
flags.DEFINE_separatedlist('ID',None,'Either Screen name or user id')
#flags.DEFINE_string('screen_name',None,'ENter the screen name')
flags.DEFINE_output('user_profile',None,'Returns user profile in JSON format')
flags.DEFINE_output('output_dir','','The output dir')


def main(args):
    t=ta.authorize()
    print "The authorized token is %s"%t
    print au.FLAGS['screen_name']
    user_profile=up.get_user_profile(t,au.FLAGS['screen_name'],au.FLAGS['ID'])
    with open(au.OUTPUT['user_profile'],'w') as fh:
        json.dump(user_profile,fh,indent=1)

    
if __name__=="__main__":
    au.run(main)
