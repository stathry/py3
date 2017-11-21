'''
Created on 2017年11月21日

@author: dongdaiming
'''
import logging


ns = iter([5,3,1,0])
while True:
    try:
        print(1.0/next(ns))
    except Exception as e:
        logging.exception(e)
        break