#-*- coding: utf-8 -*-
'''
Created on 2017-11-30

@author: YuPeng
'''
import redis

r = redis.Redis(host='198.218.6.165', port=10001, decode_responses=True)
print(r.get('QO_KW_ytest99'))
print(r.get('honour_20171203#D311#4#'))