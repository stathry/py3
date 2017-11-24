'''
Created on 2017年11月21日

@author: dongdaiming
'''

class people:
    username=''
    age=0
    
    def __init__(self, username, age):
        self.username = username
        self.age = age
    
    def learn(self, language):
#         print('Hi ' + self.username + "'!It's time to learning " + language)
        print("Hi %s! you are %d years old,It's time to learning %s." %(self.username, self.age, language))
        
# p = people('scofx', 27)        
# p.learn('python')

class student(people):
    school=''
    no=''
    def __init__(self, username, age, school, no):
        self.username = username
        self.age = age
        self.school = school
        self.no = no
    
    def study(self, language):
        print("I am a student of s%, student no s%,I am studying s%." %(self.school, self.no, language))
        
s = student('scofx', 27, 'MIT', '863')        
s.study('python')