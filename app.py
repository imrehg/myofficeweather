#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import requests
from flask import Flask
from flask import request
app = Flask(__name__)


APIKEY=os.environ['APIKEY']
FLOW=os.environ['FLOW']
PROXYKEY=os.environ['PROXYKEY']

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/', methods=['POST'])
def repost():
    data = json.loads(request.data)
    message = json.loads(data['message'])
    content = "Current office temperature: {}°C [bot]".format(message['temperature'])
    if PROXYKEY != message['proxykey']:
        response = "Bad luck!"
        return response, 401
    payload = {'event': 'message', 'content': content}
    r = requests.post("https://api.flowdock.com/flows/{}/messages".format(FLOW), json=payload, auth=(APIKEY, ''))
    print(r.json())
    return "Done"

if __name__ == '__main__':
    app.run()
