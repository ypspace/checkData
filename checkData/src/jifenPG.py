#-*- coding: utf-8 -*-
'''
Created on 2017-12-4

@author: YuPeng
'''
import web, psycopg2

urls = (
        '/', 'index',
        '/jifenpg', 'jifenPG'
        )

render = web.template.render('templates/')

def selectTable(db_cur, table_name, sql):
    db_cur.execute(sql)
    column_names = [desc[0] for desc in db_cur.description]
    row_item = db_cur.fetchall()
    res_set = []
    for i in row_item:
        row = []
        for l in i:
            #print l
            row.append(l)
            #print chardet.detect(l)
        res_set.append(row)
    table = {
            "title": table_name,
            "column": column_names,
            "data": res_set
            }
    return table

class index:
    def GET(self):
        return render.index()
    
class jifenPG:
    def GET(self):
        params = web.input()
        member_id = params.member_id
        pg_conn = psycopg2.connect(host="198.218.35.11", port="5432", user="postgres", password="123456", database="crm")
        #pg_conn = psycopg2.connect(host="198.218.6.169", port="5432", user="postgres", password="postgres", database="hbdp")
        pg_cur = pg_conn.cursor()
        table_name = "point.crm10_cumulate_train_info"
        pg_sql = "SELECT * FROM "+table_name+" WHERE member_id='"+member_id+"'"
        crm10_cumulate_train_info = selectTable(pg_cur, table_name, pg_sql)
        
        table_name = "center.crm10_train_point_log"
        pg_sql = "SELECT * FROM "+table_name+" WHERE member_id='"+member_id+"'"
        crm10_train_point_log = selectTable(pg_cur, table_name, pg_sql)
        
        table_name = "point.crm10_cumulate_simple"
        pg_sql = "SELECT * FROM "+table_name+" WHERE member_id='"+member_id+"'"
        crm10_cumulate_simple = selectTable(pg_cur, table_name, pg_sql)
        
        table_name = "point.crm10_member_point_summary"
        pg_sql = "SELECT * FROM "+table_name+" WHERE member_id='"+member_id+"'"
        crm10_member_point_summary = selectTable(pg_cur, table_name, pg_sql)
        
        all_tables = (crm10_cumulate_train_info, crm10_train_point_log, crm10_cumulate_simple, crm10_member_point_summary)
        
        pg_cur.close()
        pg_conn.close()
        return render.showdata(all_tables)

    
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
