# encoding = utf-8
# author：Simon

import requests
import json
from wxpy import *


def auto_ai(text):
    url = 'http://www.tuling123.com/openapi/api'
    api_key = '6e18e494b00e46deb90b2e0cdd5b6d8d'
    payload = {"key": api_key, "info": text, "userid": "小蝎子"}
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result['text']


def auto_ai2(text):
    url = 'http://www.tuling123.com/openapi/api'
    api_key = '4ce1451fa18f4c4fa906a65c2c149c51'
    payload = {"key": api_key, "info": text, "userid": "小蝎子"}
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result['text']


bot = Bot(cache_path="E:\pythonLearning\wxrobot\wxrobot.pkl")
mygroup = bot.groups().search('斧头帮')
for member in mygroup:
    @bot.register(member)
    def recGroups(msg):
        print(msg)
        if msg.type == 'Text':
            reply = auto_ai(msg.text)
        elif msg.type == 'Picture':
            reply = '请讲普通话，说中文'
        elif msg.type == 'Recording':
            reply = '听不懂你说啥，请用文字和我交流'
        else:
            reply = '什么东西辣眼睛！[害羞]'
        print('reply msg: %s' % reply)
        return reply

mygroup2 = bot.groups().search('242班')
for member in mygroup2:
    @bot.register(member)
    def recGroups(msg):
        print(msg)
        if msg.type == 'Text':
            reply = auto_ai2(msg.text)
        elif msg.type == 'Picture':
            reply = '请讲普通话，说中文'
        elif msg.type == 'Recording':
            reply = '听不懂你说什么，请用文字和我交流'
        else:
            reply = '什么东西辣眼睛！[害羞]'
        print('reply msg: %s' % reply)
        return reply
embed()




