import requests
import json
import facebook
def pp(o):
    print json.dumps(o,indent=1)
ACCESS_TOKEN='CAACEdEose0cBANaCZBJTy39oDB81xM3wTNLpOh20HMb32tdFAH8h6NGvYTQPCoJWFndZB6dIYO0QitoaAciJzHT254eRFsgwN3AGi1ssNIoTAYZCombKlBPq71hvoKiQ2D4rjqMZCP0sQu6PIeIt2fQ04VTwwya2aCwlM6GpGcqdVbY5JVAuHFt7aAiY7UxIzG8l0hM6IQZDZD'
g=facebook.GraphAPI(ACCESS_TOKEN)
print g
pp(g.get_object('me'))
print "other user#####################################"

pp(g.get_object('85198421191'))

print "connections####################################################"
pp(g.get_connections('10201396334829301','friends'))

print "search result################################"
#pp(g.request("search",{'q':'knoxnews','type':'page'}))


print "feeds and links"
#pp(g.get_connections('PepsiUS','feed'))

#print "##############################################"
#pp(g.get_connections('PepsiUS','links'))
#print "##############################################"
#pp(g.get_connections('knoxnews','links'))
#print "##############################################"

#pp(g.get_connections('CocaCola','feed'))
print "##############################################"
pp(g.get_connections('knoxnews','feed'))

