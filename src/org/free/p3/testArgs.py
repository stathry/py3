'''
Created on 2017年11月20日

@author: dongdaiming
'''

def fun1(p1, *args):
    print('p1:' + str(p1))
    for x in args:
        print('args:' + str(x))
    
        
# fun1('v1')        
# fun1('v2', 'a1', 'a2')        


def fun2(p1, **args):
    print('p1:' + str(p1))
    for k in args:
        print('args:k:' + str(k) + ',v:' + str(args[k]))
    
        
# fun2('v1')        
# fun2('v2', n1='a1', n2='a2')        


def fun3(p1, p2=10):
    print('p1:' + str(p1))
    print('p2:' + str(p2))
    
        
# fun3('v1')        
fun3('v2', 2)        