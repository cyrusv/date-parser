#!/bin/python

import requests
import sys

r = requests.get('http://localhost:5000', data={'q': sys.argv[1]})
if r.ok:
    print(r.content)
else:
    print(r)
