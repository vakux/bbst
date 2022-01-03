#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import base64
import re
import requests
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', help='鏌ヨ璇硶', dest="query")
    args = parser.parse_args()

    s = args.query

#    print (s)
    encodestr = base64.b64encode(s.encode('utf-8'))
    s1 = str(encodestr, 'utf-8')
    api = "https://fofa.so/api/v1/search/all?email=1054980493@qq.com&key=c44cb3180fc26a5d0bf6efcef428af79&qbase64=%s&size=10000" % s1
#   print (api)

    response = requests.get(api)
 #   print(response.text)

    res = json.loads((response.content).decode('utf-8'))
#   print (res["error"])
#   print (res["size"])


    if res["error"] == "False":
        print("error in query :  " + s)
        return
    else :
        if res["size"] >= 10000:
            print (s + "  result more than 10000")
        else:
            resulits = res["results"]
            for i in resulits:
                print (i[0])


if __name__=='__main__':
    main()

