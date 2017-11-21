'''
Created on 2017年11月20日

@author: dongdaiming
'''


def printc(c):
    if(isinstance(c, dict)):
        for x in c.keys():
            print(c[x])
    elif(isinstance(c, list) or isinstance(c, tuple)):
        for x in c:
            print(x)
    else:
        print(str(type(c)) +' is not a dict or list.')
    return


# printc({'name':'香菇鸡', 'age':18, 'birth':'2017-11-20'})
# printc([1,3,5])
# printc((2,4,6))
printc('hello')