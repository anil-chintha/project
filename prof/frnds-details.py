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
connections = app.get_profile(selectors=['positions'])
#print json.dumps(my_positions, indent=1)

connection_id = connections['values'][0]['id']
connection_positions = app.get_profile(member_id = connection_id) 
#                                       selectors=['positions'])
# print json.dumps(connection_positions, indent=1)

# ----------------------------------------------

for h in range(15):
   frnd=frndrqst['data'][h]['id']
   frnddtls=g.get_object(frnd)
   a=frnddtls.keys()
   ab=frnddtls.values()
   keylen=len(a)
   count=0

for l in range(keylen):
       if(a[l]=='birthday'):
          count=1

   if(count==1):
       print "all attributes are present"
p5=userfrnddetls(username=frnddtls['username'],firstname=frnddtls['first_name'],
lastname=frnddtls['last_name'],name=frnddtls['name'],gender=frnddtls['gender'],birthday1=frnddtls
['birthday'])
       p5.save()

   else:
         a[keylen-1]='birthday'
         ab[keylen-1]=''
        
p5=userfrnddetls(username=frnddtls['username'],firstname=frnddtls['first_name'],
lastname=frnddtls['last_name'],name=frnddtls['name'],gender=frnddtls['gender'],birthday1=ab[keylen-1])
         p5.save()

# ---------------------------------------------------------------------------


rng = len(connections['values'])
for u in range(rng):
  r = connections['values'][u]['id'] 
  s = connections['values'][u]['firstName']
  t = connections['values'][u]['location']

   # frnddtls=app.get_connections(r)
   a=frnddtls.keys()
   ab=frnddtls.values()
   keylen=len(a)
   count=0

       for l in range(keylen):
           if(a[l]=='location'):
              count=1

         if(count==1):
             print "connections with locations"
             re = prof(header=t,proid=r,proname=s)
             re.save()

         else:
              a[keylen-1]='location'
              ab[keylen-1]=''
              
re = prof(header=t,proid=r,proname=ab[keylen-1])
re.save()




#for l in range(keylen):
#       if(a[l]=='location'):
 #         count=1

#if(count==1):
#  print "connections with locations"
#else:

#a[keylen-1]='location'
#ab[keylen-1]=''
#print 


