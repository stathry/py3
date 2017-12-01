'''
Created on 2017年12月1日

@author: dongdaiming
'''

def generator():
    for x in range(5):
        yield x * x

l = generator()
print(type(l))        
for n in l:
    print(n)        