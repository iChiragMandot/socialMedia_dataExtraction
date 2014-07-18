import authorize as a
from au import au,flags

flags.DEFINE_string('API_KEY',None,'Takes the API Key assigned to the application')
def main(args):
    API_KEY=au.FLAGS['API_KEY']
    gp_api=a.authorize(API_KEY)

if __name__=="__main__":
    au.run(main)
    
