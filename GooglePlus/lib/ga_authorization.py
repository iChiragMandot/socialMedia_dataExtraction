import apiclient.discovery
import httplib2
def authorize():
    API_KEY='AIzaSyDTXm7tMT1UFLbpmxBE9dh2vgvAepdFOxc'
    return apiclient.discovery.build('plus','v1',http=httplib2.Http(),developerKey=API_KEY)
