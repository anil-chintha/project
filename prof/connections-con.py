from linkedin import linkedin
from prof.models import prof
#from linked.models import search_company
import json
CONSUMER_KEY = '75nanr9qwylt2d'
CONSUMER_SECRET = 'UpORpgoDH1iUl2kL'
USER_TOKEN = '5767f0eb-881b-4d79-ba40-7a191856890c'
USER_SECRET = '2132991c-9e73-4ef1-b83c-9dbb64113b0b'
RETURN_URL = ' http://127.0.0.1:8000/'
auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums
.values())
app = linkedin.LinkedInApplication(auth)
connections = app.get_connections()

rng = len(connections['values'])
for u in range(rng):
  r = connections['values'][u]['id'] 

        
for u in range(rng):
    r = connections['values'][u]['id']
    s = connections['values'][u]['location']
    print r
    print s
    if r == 'private':
        continue
        print r
            



   for y in r:
             if y == 'private':
               continue
               connections = app.get_connections()
               limt = len(connections['values']
                 for w in range(limt): 
                 z = connections['values'][u]['id']
               print z

               #con = app.get_connections()
               # second = len(connections['values']
               # for v in range(second):
               #  m = con['values'][v]['id']
               #  n = con['values'][v]['id']
 
               #print m
               # print n

  # re = prof(header=t,proid=r,proname=s)
  # re.save()
