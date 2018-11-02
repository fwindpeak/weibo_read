#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
import sys


URL_ROOT = 'https://m.weibo.cn'


def getCardList(uid):
    url = URL_ROOT + "/api/container/getIndex?type=uid&value=%s" % (uid)
    data = requests.get(url).json()
    for tab in data['data']['tabsInfo']['tabs']:
        if tab['title'] == '微博':
            containerid = tab['containerid']
    page = 0
    while True:
        page += 1
        url = url + "&containerid=%s&page=%s" % (containerid, page)
        data = requests.get(url).json()
        cards = data['data']['cards']
        if len(cards) < 1:
            break
        for card in cards:
            if card['card_type'] == 9:
                yield processMblog(card['mblog'])


def processMblog(mblog):
    create_at = mblog['created_at']
    text = ''
    if mblog['isLongText'] is False:
        text = mblog['text']
    else:
        url = URL_ROOT + "/statuses/extend?id=%s" % (mblog['id'])
        text = requests.get(url).json()['data']['longTextContent']
    return "%s\n%s" % (create_at, text)


def cleanText(text):
    text = re.sub('<br.*?>', '\n', text)
    text = re.sub('<.+?>', '', text)
    return text


def main():
    if len(sys.argv) < 2:
        uid = input("uid:")
    else:
        uid = sys.argv[1]
    for t in getCardList(uid):
        print(cleanText(t))
        print("-"*20)


if __name__ == '__main__':
    main()
