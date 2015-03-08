'''
Created on Sep 5, 2014

@author: Deena Rubin
'''
from agent_ai.agent import *
from agent_ai.text import process_text

user = human()
user.set_name()
eliza = eliza(user)
game_over = False

response = eliza.greeting()
if response == 'bye':
    game_over = True

while not game_over:
    response = process_text(response)
    response = eliza.communicate(response)
    if response == 'bye':
        game_over = True
    
eliza.finished()

   





