#-*- coding: utf-8 -*-
'''
Created on 2017-12-4

@author: YuPeng
'''
import web, psycopg2, chardet

urls = (
        '/', 'index',
        '/connectpg', 'connectPG'
        )

render = web.template.render('templates/')

class index:
    def GET(self):
        return "Hello, world!"
    
class connectPG:
    def GET(self):
        pg_conn = psycopg2.connect(host="198.218.35.11", port="5432", user="postgres", password="123456", database="crm")
        pg_cur = pg_conn.cursor()
        pg_sql = "SELECT * FROM point.crm10_cumulate_simple WHERE member_id='021076400069'"
        pg_cur.execute(pg_sql)
        column_names = (desc[0] for desc in pg_cur.description)
        #print column_names
        row_item = pg_cur.fetchall()
        '''
        for i in row_item:
            for l in i:
                print type(l)
                print chardet.detect(l)
        '''
        pg_cur.close()
        pg_conn.close()
        params = {'title': column_names, 'row': row_item}
        #return render.showdata(str, params)
        return render.showdata(column_names, row_item, str)
    
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()