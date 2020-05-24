import requests
import json

#API_URL = "http://127.0.0.1:5000/upload"
#API_URL = "http://127.0.0.1:5000"
API_URL = "https://3exiqyk1s2.execute-api.ap-south-1.amazonaws.com/dev/"
API_KEY = '152-375-929'


headers = {'apikey': API_KEY}

with open('file.pdf', 'rb') as fp:
    content = fp.read()

response = requests.post(API_URL, headers=headers, data=content)

print(response.text)
"""
jdata = json.loads(response.text)
print(jdata["status"])
for p in jdata["pages"]:
    print (p)
    print("")
    print("")
    print("")
    print("")
"""
#print(type(response.text))
#for page in response.text["text"]:
#    print(page)


"""
headers = {
    'Username': 'abc@gmail.com', 
    'apikey':'152-375-929',
    'accept-encoding': "gzip, deflate, br",
    'accept': "*/*",
    'content-type': "multipart/form-data; boundary=<calculated when request is sent>"
    }
"""

"""
import requests
from requests.auth import HTTPBasicAuth
import json
from pathlib import Path

file_ids = ''
headers={'Username': 'abc@gmail.com', 'apikey':'123-456'}
# Upload file

f = open('C:/Users/ADMIN/Downloads/abc.zip', 'rb')

files = {"file": ("C:/Users/ADMIN/Downloads/abc.zip", f)}

resp = requests.post("https:// ../analytics/upload_file", files=files, headers=headers )
print resp.text
print "status code " + str(resp.status_code)

if resp.status_code == 201:
    print ("Success")
    data = json.loads(resp.text)
    file_ids = data['file_ids']
    print file_ids
else:
    print ("Failure")
"""