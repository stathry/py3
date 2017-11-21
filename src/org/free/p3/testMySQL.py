'''
Created on 2017年11月21日

@author: dongdaiming
'''

import pymysql

conn = pymysql.connect(
    host='localhost', port=3306, user='root', passwd='root', db='test')
cursor = conn.cursor()
## version
# cursor.execute('select version()')
# row = cursor.fetchone()
# print(row[0])

## insert
# r = cursor.execute("insert into zm_score_acc(user_id,zm_score) values('666', '888')")
# conn.commit()
# print(r)
# conn.close()

## delete
# r = cursor.execute("delete from zm_score_acc where id=1949")
# conn.commit()
# print(r)
# conn.close()

## update
r = cursor.execute("update zm_score_acc set zm_score='521' where id=2")
conn.commit()
print(r)
conn.close()

## select
# cursor.execute('select user_id,zm_score from zm_score_acc limit 2')
# rows = cursor.fetchall()
# for row in rows:
#     print('user_id:' + str(row[0]))
#     print('zm_score:' + str(row[1]))

