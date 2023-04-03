import requests
import json
from pprint import pprint

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
print(response)
print(response['result']['body']['TABLE_interface']['ROW_interface']['admin_state'])