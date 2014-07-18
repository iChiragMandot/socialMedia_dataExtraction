import searchProfile
import ga_authorization as ga
from au import au,flags
import httplib2
import json
import apiclient.discovery

flags.DEFINE_string('search_term',None,'Search Term')
flags.DEFINE_output('people_profile',None,"Person's profile is returned")
flags.DEFINE_output('output_dir','','The output dir')

def main(args):
    service_key=ga.authorize()
    print service_key
    person_profile=searchProfile.searchF(service_key,au.FLAGS['search_term'])
    with open(au.OUTPUT['people_profile'],'w') as fh:
        json.dump(person_profile,fh,indent=1)

if __name__=="__main__":
    au.run(main)

