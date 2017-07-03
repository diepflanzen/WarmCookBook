#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pip install facebook-sdk

import facebook

# 用 https://findmyfbid.com 找出Event列表的id
ID = '349696661821984'
filename = '紐約哲五.txt'

# 爬出這個ID的網頁的資料
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAOu3jeqZC59SNSNINpOnhs4b9UZCrYuvygnYgvyaAsTsUPsqkM7qASkZBoHZBD2DxmXpoHXta8k3Xz1HiKmG6AlvBkQowAvMELGWaGqD9dluNWXMQUSZBVaraOhvrOUdamuaht8RBWrSTvs2cpevTujqiFoxyZC2jQY2gCZAbZAJ8L6xwX2b6zEZD', version='2.7')
a = graph.get_object( ID + '/events?limit=50')


# 開一個文字檔
with open(filename, 'w') as f:

    # 在剛剛那個網頁的資料裡面每一個Event
    for event in a['data']:

        # 找出"description"的內容
        d = event['description']
        
        # 找到符合【主題】.....的字串
        s = d.find(u'【主題】')
        sa = d.find(u'【', s+1)
        ss = d[s:sa]
        
        # 找到符合【主講人】.....的字串
        t = d.find(u'【主講人】')
        ta = d.find(u'【', t+1)
        tt = d[t:ta]
        
        # 找到符合【內容簡介】.....的字串
        v = d.find(u'【內容簡介】')
        va = d.find(u'【', v+1)
        vv = d[v:va]
        
        # 把剛剛那三行用逗點分隔，寫進剛開的文字檔裡面。
        k = ' ,'.join([ss, tt, vv])
        f.write(k.encode('utf8')) 
