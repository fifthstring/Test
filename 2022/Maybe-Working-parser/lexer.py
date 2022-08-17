
import re
reg = '\\b|(\\(.*?\\))'
reg2 = "\\b|(\\(|\\))"
valid_str_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?,.;:_'
functions = ['lower', 'upper', 'input', 'length']
keywords = ['delay','if', 'display','input','loop','break','else']
operators = ['+','-','*','/','>','<','>=', '<=', '!=','==','%', '&', '|','^']
assigner = ["="]
paren = [ ')', '(']
sep = [';', '/']


def lex(raw_data=open('input.txt').read(), reg="\\n|\\b|(\\()|(\\))|(\\'.*?\\')"):
    regexed_data = re.split(reg, raw_data)
    
    regexed_data=  [i for i in regexed_data if i and i.replace(' ','') and i != '\n' ]

    tokens = []
    for i in regexed_data:
        if i.isnumeric():
            tokens.append(['integer', i])
        elif i.replace('.','').isnumeric():
            tokens.append(['float', i])
        elif i.replace(' ','') in functions:
            tokens.append(['function', i])
        elif i.replace(' ','') in operators:
            tokens.append(['operator', i])
        elif i.replace(' ','') in assigner:
            tokens.append(['assignment', i])

        elif i.replace(' ','') in sep:
            tokens.append(['separator', i])

        elif i.replace(' ','') in keywords:
            tokens.append(['keyword', i])
        elif i.replace(' ','') in paren:
            tokens.append(['paren', i])

        elif i.replace(' ','')[0] == "'" and i.replace(' ','')[-1] == "'":
            tokens.append(['string', i[1:-1]])
        
        

        elif False not in [j in valid_str_chars for j in i]:
            tokens.append(['variable', i])


        elif i.replace(' ','').replace('\n','') in ('}', '{'):
            tokens.append(['separator', i.replace(' ','').replace('\n','')])

        else:
            pass

            #print('Invalid token', i)
            #exit()

    return tokens


    