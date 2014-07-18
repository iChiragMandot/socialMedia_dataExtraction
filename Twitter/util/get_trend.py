#INPUT: location id (generated from Yhoo Earth Locator)
#OUPUT: Trends in the specified location

import find_trends as ft
import json
from au import flags,au
import twitter_acc_authorization as ta


flags.DEFINE_string('location_id',None,'Give location ID from Yahoo Earth Locator| WOE_ID')
flags.DEFINE_output('trends_json',None,'Returns the trends in the specified location')
flags.DEFINE_output('output_dir','','the output dir')


def main(args):
    t=ta.authorize()
    trends=ft.search_trends(t,au.FLAGS['location_id'])
    with open(au.OUTPUT['trends_json'],'w') as fh:
        json.dump(trends,fh,indent=1)

    
    if __name__=="__main__":
    au.run(main)
