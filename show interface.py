import requests
import json

"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.

switchuser='admin'
switchpassword='Lock&Key()19'


url='https://172.26.21.101/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show int eth 1/4",
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()
print (response)