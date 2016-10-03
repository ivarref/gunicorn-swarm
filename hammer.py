#!/usr/bin/env python

from __future__ import print_function
import requests
import sys
import signal
from sets import Set

if __name__=="__main__":
    print('hammer.py running ...')
    ok = 0
    items = Set()
    while True:
        try:
            response = requests.get('http://localhost:8080/')
            if len(response.text) == 36:
                ok += 1
                items.add(response.text)
            else:
                print('incorrect response, was', response.text)
                raise ValueError('Incorrect response', response.text)
        except:
            raise
        finally:
            sys.stdout.write("\rOK: %d, unique items: %d" % (ok, len(items)))
            sys.stdout.flush()
