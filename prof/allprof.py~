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
  s = connections['values'][u]['firstName']
  t = connections['values'][u]['location']

  re = prof(header=t,proid=r,proname=s)
  re.save()


#result = prof(firstname=x['firstName'],lastname=x['lastName'])
 #result.save()
 


# y = profile(header=x['header'],proid=x['id'],proname=x['name'])

# print connections
#x = connections('header')
# connections = app.get_profile('header')
# connections = app.get_profile('rmRc7zfsQX')
# print connections

