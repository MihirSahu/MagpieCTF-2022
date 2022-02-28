#!/usr/bin/env python3

import requests

'''
1. Client connects to the vault
2. Vault replies: "oh hai!"
3. Client sends: "INITIALIZE CONNECTION"
4. Vault replies: "Connection successfully initialized. Please reply with request..."
5. Client replies: "SEND FLAG"
6. Vault replies: "Flag requested. Reply with challenge string <string>"
7. Client replies: "<string>"
8. Vault replies with encrypted flag data
'''

vaults = ["http://vault1.momandpopsflags.ca", "http://vault2.momandpopsflags.ca", "http://vault3.momandpopsflags.ca"]

# Connect to the vault
connect = requests.get("http://vault1.momandpopsflags.ca:9100", params={"hi": "INITIALIZE CONNECTION"})
print(connect.content)
