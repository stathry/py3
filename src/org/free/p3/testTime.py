'''
Created on 2017年11月20日

@author: dongdaiming
'''

import time
import datetime
import calendar

d = time.localtime()
d2 = datetime.datetime.now()
print(calendar.calendar.format('%Y-%m-%d %H:%M:%S', d))
# print(time.strftime('%Y-%m-%d %H:%M:%S', d))
# print(d2.year)
# print(d2)
# print(datetime.datetime.isoformat(d2))
# print(time.asctime(d))
# print(time.time())
