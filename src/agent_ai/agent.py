'''
Created on Sep 5, 2014

@author: Deena Rubin
'''

class human(object):
    
    def set_name(self):
        self.name = input('Hi, I\'m Eliza, what is your name? ')
    

        

class eliza(object):
    
    def __init__(self, user):
        self.user = user
    
    def greeting(self):
        return input( 'Hi, ' + self.user.name + ', what would you like to talk about today? ')
    
    def communicate(self, text):
        return input(text)
    
    def finished(self):
        print ('bye, ' + self.user.name + ' come back soon!')
        