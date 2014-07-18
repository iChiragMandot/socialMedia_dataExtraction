import requests
import json
ACCESS_TOKEN='CAACEdEose0cBAI0Rz42eW92NulxdD9thaeLwAoa8ynQkmr0At5MjAumOuYynvnSAfO5BlBWKVmnzjXbe7jgi2DvS5q5UvcfZBWVCHXIiMYJlKtmbwyzcjD4mJsukBS7XkW27JZCvWZB1g6UZCZCx62oyNGLivReBF022ZALE3mylwLeTE77nPCVR8ySluIp1nukmiTsb6gwwZDZD'
base_url='https://graph.facebook.com/'
fields='id,name,friends.fields(likes)'
#url='%s/%s?fields=%s&access_token=%s'%(base_url,fields,ACCESS_TOKEN,)
#print url
page_id='knoxnews/'
url='%s/%s?fields=posts&access_token=%s'%(base_url,page_id,ACCESS_TOKEN)
data=requests.get(url).json()
with open("//root/new_social_media/fb_knox.json",'w') as fh:
    json.dump(data,fh,indent=1)

