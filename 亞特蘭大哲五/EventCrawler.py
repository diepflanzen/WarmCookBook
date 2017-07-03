#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pip install facebook-sdk

import facebook

# 用 https://findmyfbid.com 找出Event列表的id
ID = '1475967705762464'
groupname = u'亞特蘭大哲五'
csvname = groupname + '.csv'
txtname = groupname + '.txt'

# 爬出這個ID的facebook page 的 event 資料（access token 這樣取得： https://developers.facebook.com/tools/explorer/?method=GET&path=me%3Ffields%3Did%2Cname&version=v2.9）
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAOaDklSCJjZCbQ9Shwe1zDsBIdnoNj4BGVsPVZAmtdYBHhZAUWMLoBYlD6mWwN1Q50tpAMTOFE20pWDnVR52CBF1N8OZBefZByJZBZCm6kjx5OjpPciao3gLPwqJF3y9yrUO8BccZARuqXJwxfWKNZCa3ZCNPwYzwz52RrjfEQi0MexOh2CNEBiu8ZD', version='2.7')
a = graph.get_object( ID + '/events?limit=50')


# 開一個spreadsheet檔
with open(csvname, 'w') as f:

    # 在剛剛那個網頁的資料裡面每一個Event
    for event in a['data']:

        #需要的資料：題目, 講者, 時間

        # 找出"name"的內容 (就是Event title)
        issue_content = event['name']


        # 找出"start_time"的內容 (2017-07-07T21:00)
        time_content = event['start_time']
        time_start = time_content.find(u'2')
        time_end = time_content.find(u'T')
        time = time_content[time_start:time_end]


        # 找出"description"的內容
#        description_content = event['description']
       
        
#        # 找到符合'【主講人】.....【 '的字串
#        speaker_start = description_content.find(u'講者')
#        speaker_end = description_content.find(u'|', speaker_start+1)
#        speaker = description_content[speaker_start:speaker_end]
        speaker = ''
        
        # 把剛剛那行用逗點分隔，寫進剛開的spreadsheet檔裡面。
        to_print = ', '.join([issue_content, speaker, groupname, time])
        f.write(to_print.encode('utf8')) 
        f.write('\n')

#開一個文字檔
with open(txtname, 'w') as f:

    # 在剛剛那個網頁的資料裡面每一個Event
    for event in a['data']:

        #需要的資料：題目, 講者, 時間

        # 找出"name"的內容 (就是Event title)
        issue_content = event['name']

        # 找出"start_time"的內容 (2017-07-07T21:00)
        time_content = event['start_time']
        time_start = time_content.find(u'2')
        time_end = time_content.find(u'T')
        time = time_content[time_start:time_end]


        # 找出"description"的內容
        try:
            description_content = event['description']
        except:
            description_content = ''
                        
        # 把題目，時間，description，寫進剛開的文字檔裡面。
        to_print = '%s \n %s \n---\n %s \n===\n' %(issue_content, time, description_content)
        f.write(to_print.encode('utf8')) 



