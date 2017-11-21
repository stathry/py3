'''
Created on 2017年11月21日

@author: dongdaiming
'''

import pymysql

conn = pymysql.connect(
    host='localhost', port=3306, user='root', passwd='root', db='test')
cursor = conn.cursor()
# cursor.execute('select version()')
# row = cursor.fetchone()
# print(row[0])
cursor.execute('select user_id,zm_score from zm_score_acc limit 2')
rows = cursor.fetchall()
for row in rows:
    print('user_id:' + str(row[0]))
    print('zm_score:' + str(row[1]))

