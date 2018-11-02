#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
import sys


def getCardList(uid):
    url_start = "https://m.weibo.cn/api/container/getIndex?type=uid&value=%s" % (uid)
    data = requests.get(url_start).json()
    for tab in data['data']['tabsInfo']['tabs']:
        if tab['title'] == '微博':
            containerid = tab['containerid']

    url = "%s&containerid=%s" % (url_start, containerid)
    data = requests.get(url).json()
    for card in data['data']['cards']:
        if card['card_type'] == 9:
            yield processMblog(card['mblog'])


def processMblog(mblog):
    if mblog['isLongText'] is False:
        return mblog['text']
    else:
        url = "https://m.weibo.cn/statuses/extend?id=%s" % (mblog['id'])
        return requests.get(url).json()['data']['longTextContent']


def cleanText(text):
    tag_list = ['span', 'a', 'div', 'p']
    for tag in tag_list:
        text = re.sub('<%s.+?</%s>' % (tag, tag), '', text)
    text = re.sub('<br.*?>', '\n', text)
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
