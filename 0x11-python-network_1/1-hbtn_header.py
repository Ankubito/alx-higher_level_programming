#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL, and displays the value of the X-Request-Id
variable found in the header of the response.
"""
import sys
from urllib import request

if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
