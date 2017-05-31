# -*- coding: utf-8 -*-

import requests

def get_data():
    url = 'http://www.3w3n.com/showPriceDefaultList'
    payload = {'r':'AF2156CCC28BAF2FA8F9D62AEAAF0D7C'}
    headers = {'Host':"www.3w3n.com",
                'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0",
                'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                'Cookie':"UM_distinctid=15c535e1aa7151-057ae2cd5b8aa3-3e6e4647-c0000-15c535e1aa895; CNZZDATA3767539=cnzz_eid%3D878788885-1496043905-http%253A%252F%252Fwww.3w3n.com%252F%26ntime%3D1496209511; JSESSIONID=24791B3A52F61ACE4FD786444D519B6C",
                'Accept-Language':"en-US,en;q=0.5",
                'Accept-Encoding':"gzip, deflate",
                'Connection':"keep-alive",
                'Upgrade-Insecure-Requests':"1"}
    r = requests.get(url,params=payload,headers=headers)
    print r.text


if __name__ == '__main__':
    get_data()
