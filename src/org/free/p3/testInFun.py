'''
Created on 2017年11月21日

@author: dongdaiming
'''

# print(bin(4))
# print(bool(2))
# print(type(bool(2)))
# print(issubclass(bool, int))
# print(chr(97))
# print(chr(65))

# d= dict({'a':'a1', 'b':'b1'})
# print(type(d))
# print(d)
# print(dir(str))
# x=3
# print(eval('x * 2 + 1'))
# if(os.path.exists('/temp/py3/a')):
#     print('file exists.')
# else:
#     os.makedirs('/temp/py3/a', 777)

# def luck(n):
#     return n % 6 == 0 or n % 8 == 0
# 
# luckn=filter(luck, range(1,50))
# 
# for x in luckn:
#     print(x)

# s = 'hello {user}! your birthday is {birth}.'.format(
#     birth='1990-9-9', user='ddm')
# print(s)

# print(hash(10))
# n=100
# print(id(n))
# print(type(id(n)))
# print(issubclass(bool,int))
t=(1,3,5)
for x in iter(t):
    print(x)
