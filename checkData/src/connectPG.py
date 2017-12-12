#-*- coding: utf-8 -*-
'''
Created on 2017-11-30

@author: YuPeng
'''
import psycopg2

pg_conn = psycopg2.connect(host="198.218.6.169", port="5432", user="postgres", password="postgres", database="hbdp")
pg_cur = pg_conn.cursor()
pg_sql = "select * from hb10_reserve_list_brief"
pg_cur.execute(pg_sql)
column_names = [desc[0] for desc in pg_cur.description]
print column_names
#print("Column names: {}\n".format(column_names))
'''
for desc in pg_cur.description:
    print desc.name
print pg_cur.rowcount
#row_item = pg_cur.fetchone()
'''
row_item = pg_cur.fetchall()
for i in row_item:
    print i
'''
while row_item != None:
    row_str = ''
    for key in row_item:
        row_str = row_str + str(key) +','
    print row_str.decode('gbk')
'''
pg_cur.close()
pg_conn.close()