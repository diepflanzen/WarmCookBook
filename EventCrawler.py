#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pip install facebook-sdk

import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAL3kCNWRLe5gHMa6NycDoaqZCce9940ajubcI7blyM8eUqGztl4iapk0G7xloX4bVaylTYYmTjiiu1kQ9vvlnZAWeS3AKumAZCkZAxDpIbrjUaaYf5xzOQ8eNmlgnMYFkLhBaPdj8AC4jdKufw9bZAaHzqbUkHMMpSqLeuPu2oQOjAVQrRKoZD', version='2.7')

a = graph.get_object( '349696661821984' + '/events?limit=50')

with open('test.csv', 'w') as f:
    for event in a['data']:
        d = event['description']
        s = d.find(u'【主題】')
        sa = d.find(u'【', s+1)
        ss = d[s:sa]
        t = d.find(u'【主講人】')
        ta = d.find(u'【', t+1)
        tt = d[t:ta]
        v = d.find(u'【內容簡介】')
        va = d.find(u'【', v+1)
        vv = d[v:va]
        k = ' ,'.join([ss, tt, vv])
        f.write(k.encode('utf8')) 
