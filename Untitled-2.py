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
print(payload[0]["params"]["version"])