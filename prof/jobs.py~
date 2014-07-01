from linkedin import linkedin
from prof.models import prof
import json

# See http://developer.linkedin.com/documents/profile-fields#fullprofile
# for details on additional field selectors that can be passed in for
# retrieving additional profile information.

# Display your own positions...
CONSUMER_KEY = '75nanr9qwylt2d'
CONSUMER_SECRET = 'UpORpgoDH1iUl2kL'
USER_TOKEN = '5767f0eb-881b-4d79-ba40-7a191856890c'
USER_SECRET = '2132991c-9e73-4ef1-b83c-9dbb64113b0b'
RETURN_URL = ' http://127.0.0.1:8000/'
auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums
.values())
app = linkedin.LinkedInApplication(auth)
my_positions = app.get_profile(selectors=['positions'])
print json.dumps(my_positions, indent=1)

# Display positions for someone in your network...

# Get an id for a connection. We'll just pick the first one.
connection_id = connections['values'][0]['id']
connection_positions = app.get_profile(member_id=connection_id, 
                                       selectors=['positions'])
print json.dumps(connection_positions, indent=1)
