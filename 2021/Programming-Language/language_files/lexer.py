import re

raw = open('input.txt').read()
raw = raw.replace('"',"'")

# TOKEN SPLITTING
# Input -> Raw data 
# Output -> 1D List of words

r = "('.*?'|\\(.*?\\)|\\b|\\n)"
string_regex = "'(.*?)'|\\((.*?)\\)|\\b|\\n"
data = re.split(r,raw)

data = [i for i in data if i and i.count(' ') != len(i) and i != '\n']


# TOKEN ASSIGNMENT
# Input -> 1D List of words
# Output -> 2D List of tokens

keywords = ['delay','if', 'display','input','loop','break', 'upper', 'lower']
operators = ['+','-','*','/','>','<','>=', '<=', '!=','==','%', '&', '|','^']
assigner = ["="]
tokens = []
valid_tokens = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.?!#@;:+-*/&^_'
for i in data:

    if i in keywords:
        tokens.append(['keyword', i])
    elif i.replace(' ','') in assigner:
        tokens.append(['assignment', i])
    
    elif i.replace(' ', '') in operators:
        tokens.append(['operator', i])
    
    
    elif True in [j in operators for j in i]:
        tokens.append(['operation', i])

    
    elif i.isnumeric() :
        tokens.append(['integer', i])
    elif i.replace(' ','') in ('}', '{'):
        tokens.append(['separator', i])
    
    elif i.replace(' ','') in (')', '('):
        tokens.append(['paren', i])

    elif False not in [i in valid_tokens for i in i.replace(' ','').replace("'",'').replace('"','')]:
        if i[0] == i[-1] == "'" or i[0]==i[-1]== '"':
            i = i[1:-1]
        tokens.append(['string', i])

    else:
        print('INVALID TOKEN', i)
        exit()
    
    


def return_tokens():
   
    return tokens
