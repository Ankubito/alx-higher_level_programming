#!/usr/bin/python3
""""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
