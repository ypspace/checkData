#-*- coding: utf-8 -*-
'''
Created on 2017-11-29

@author: YuPeng
'''
import psycopg2
import redis
import Sybase

pgcon = psycopg2.connect(database="hbdp", user="postgres", password="postgres", host="198.218.6.169", port="5432")
c = pgcon.cursor()
sql = "select * from hb10_reserve_list_brief"
c.execute(sql)
rows = c.fetchall()
for i in rows:
    print i
c.close()
pgcon.close()

r = redis.Redis(host='198.218.6.165', port=10001, decode_responses=True)
print(r.get('p_20171130_G1_M_'))
print(r.get('honour_20171201#G115#M#'))

sybcon = Sybase.connect('A2_DS', 'sa', '', 'center')
syb_c = sybcon.cursor()
syb_sql = "SELECT reserve_no,* FROM HB10_reserve_list where login_name='yupeng'"
syb_c.execute(syb_sql)
syb_rows = syb_c.fetchall()
for j in syb_rows:
    print j
syb_c.close()
sybcon.close()