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



def closing_paren(data, openPos):
    closePos = openPos
    counter = 1
    while (counter > 0):
        
        closePos += 1

        try:
            c = data[closePos][1]
            if type(c) == str:
                c=c.replace(' ', '')
        except: ''

        if (c == '('):
            counter += 1

        elif (c == ')'):
            counter -= 1


    return closePos



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
data = lex()
print(data)


def join(data, out=[]):


    i=0

    while i < len(data):
        

        if data[i][0] in ('integer', 'operator', 'operation', 'function', 'string'):
            if i + 1 < len(data):
                print(data[i], data[i+1])
                if data[i+1][0] in ('integer', 'operator', 'operation', 'function', 'string'):
                    data[i] = data[i] + data[i+1] 
                    data.pop(i+1)
                    i = i - 1
                elif data[i+1][0][0] in ('integer', 'operator', 'operation', 'function', 'string'):
                    data[i] = data[i] + data[i+1] 
                    data.pop(i+1)
                    i = i - 1
    
        else:
            out.append(data[i])
                    

            
        i += 1


    
    return data



def parse(data=lex(), out=[]):
    i = 0
    while i  < len(data):

        if data[i][0] == 'paren' and '(' in data[i][1]:
            end = closing_paren(data,i+1)

            d = data[i+1:end]
            out.append(join(parse(data = d, out = [])))
            i += len(d) + 1
            print(data[i+1])
    

        else:
            if data[i][0] != 'paren' and ')' not in data[i][1]:

                if data[i][0] == 'function':
                    data[i] += [data[i+2]]

                    data.pop(i+1)
                    data.pop(i+1)
                


                out.append(data[i])
    
        i+= 1


    return out

            
    


x = join(parse())