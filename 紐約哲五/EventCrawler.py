#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pip install facebook-sdk

import facebook

# 用 https://findmyfbid.com 找出Event列表的id
ID = '349696661821984'
groupname = u'紐約哲學星期五'
csvname = groupname + '.csv'
txtname = groupname + '.txt'

# 爬出這個ID的facebook page 的 event 資料（access token 這樣取得： https://developers.facebook.com/tools/explorer/?method=GET&path=me%3Ffields%3Did%2Cname&version=v2.9）
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAIrPxYHvjPeJwAiNDzIZC7sNKGrsFmLeglUlzmGqMYGTwruhmcwTudMmYIOirStyHZBx8fovSyiN1UiFfmAZCoO8ZBhWZC06ZC3Ab7M89MWysIMoPCY8qbxvyuZCTWbAT8IEKucoaogcZBKXBtZANIw3LCOQOj15yRD8BKi7IikUrOZAvB8PYQJL8ZD', version='2.7')
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
        description_content = event['description']
        
        
        # 找到符合'【主講人】.....【 '的字串
        speaker_start = description_content.find(u'【主講人】')
        speaker_end = description_content.find(u'\n', speaker_start+1)
        speaker = description_content[speaker_start:speaker_end]
        
        
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
        description_content = event['description']
                        
        # 把題目，時間，description，寫進剛開的文字檔裡面。
        to_print = '%s \n %s \n---\n %s \n===\n' %(issue_content, time, description_content)
        f.write(to_print.encode('utf8')) 



