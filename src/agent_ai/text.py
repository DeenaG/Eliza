'''
Created on Sep 5, 2014

@author: Deena Rubin
'''
import re
from random import choice

yes = 'yes'
yes_response = 'you are very agreeable today. Tell me more about how you are feeling. '
no = 'no'
no_response = 'you are being very argumentative. Tell me more about how you are feeling. '
end = 'bye'
present_tense = 'ing'
past_tense = 'ed'
family = ['mom', 'mother', 'dad', 'father', 'sister', 'brother', 'friend', 'cousin', 'son', 'daughter', 'niece', 'nephew', 'grandmother', 'grandfather', 'grandma', 'grandpa']
family_response = ['your xxx sounds interesting. ', 'do you like your xxx? ', 'your relationship with xxx sounds complicated. ']
negative = ['angry', 'mad', 'upset', 'sad','bad', 'bored']
negative_response = ['you sound upset. ', 'are you always so negative? ', 'maybe you need some help. ']
positive = ['happy', 'joy', 'joyful' 'good']
positive_response = ['you seem happy. ', 'being positive is good for you. ', 'that sounds exciting. ']
random_response = ['what are you doing right now? ', 'please elaborate. ', 'tell me about some people in your life. ', 'how does that make you feel? ']

def process_text(text):
    text = text.lower()
    pattern = re.compile(end)
    find_pattern = re.search(pattern, text)
    if find_pattern is not None:
        return 'bye'

    for fam in family:
        pattern = re.compile('\s' + fam + '\s' + '|' + '^' + fam + '|' + fam + '$')
        find_pattern = re.search(pattern, text)
        if find_pattern is not None:
            return choice(family_response).replace('xxx', fam)
    pattern = re.compile ('\s' + yes + '\s' + '|' + '^' + yes + '|' + yes + '$')
    find_pattern = re.search (pattern, text)
    if find_pattern is not None:
        return yes_response
    pattern = re.compile ('\s' + no + '\s' + '|' + '^' + no + '|' + no + '$')
    find_pattern = re.search (pattern, text)
    if find_pattern is not None:
        return no_response
    pattern = re.compile ('\?$')
    find_pattern = re.search (pattern, text)
    if find_pattern is not None:
        return 'Do you always ask so many questions? '
    for neg in negative:
        pattern = re.compile('\s' + neg + '\s' + '|' + '^' + neg + '|' + neg + '$')
        find_pattern = re.search(pattern, text)
        if find_pattern is not None:
            return choice(negative_response) + ' tell me more. '
    for pos in positive:
        pattern = re.compile('\s' + pos + '\s' + '|' + '^' + pos + '|' + pos + '$')
        find_pattern = re.search(pattern, text)
        if find_pattern is not None:
            return choice(positive_response) + ' tell me more. '
    pattern = re.compile('\w{1,}' + present_tense)
    find_pattern = re.search(pattern, text)
    if find_pattern is not None:
        verb = (find_pattern.group()).replace(present_tense, past_tense)
        return 'you ' + verb + '? tell me more. '
        
    
    return choice(random_response) + ' '



    
    
