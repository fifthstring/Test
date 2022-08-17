import re

def lexer(fp='input.txt'):

    # CONSTANTS BELOW
    keywords = [
    "else",
    "if",
    "while",
    "return",
    "function",
    'display',
    ]
    
    separators = [
        '{',
        '}',
        '(',
        ')',
        ',',
    ]

    operators = [
        '+',
        '-',
        '<',
        '==',
        '<=',
        '>=',
        "*",
        '/',
        '^'
    ]

    
    equals = [
        "="
    ]
    newline = [
        "\n",
        ";"
    ]
    
    # OPENING FILE

    data = open(fp).read()
    
    #The thing that defines the split 
    
    #splitby = '(\=|\+|\-|\*|\/'+ "|" + "|".join(keywords)+ "|" + "|".join(literals)+ "|" + "|".join(separators) + "|" + "|".join(newline) + ")"
    
    # REGEX 
    #print(data)
    splitby = '(=(?<!=\=)(?!\=)|\==|\+|\-|\*|\/|\^|(?<!.)else(?= )|(?<= )else(?= )|(?<=&)else(?= )|(?<!.)else(?=\\()|(?<= )else(?=\\()|(?<=&)else(?=\\()|(?<=\\})display|(?<=\\{)display|(?<!.)if(?= )|(?<= )if(?= )|(?<=&)if(?= )|(?<!.)if(?=\\()|(?<= )if(?=\\()|(?<=&)if(?=\\()|(?<=\\})display|(?<=\\{)display|(?<!.)while(?= )|(?<= )while(?= )|(?<=&)while(?= )|(?<!.)while(?=\\()|(?<= )while(?=\\()|(?<=&)while(?=\\()|(?<=\\})display|(?<=\\{)display|(?<!.)return(?= )|(?<= )return(?= )|(?<=&)return(?= )|(?<!.)return(?=\\()|(?<= )return(?=\\()|(?<=&)return(?=\\()|(?<=\\})display|(?<=\\{)display|(?<!.)function(?= )|(?<= )function(?= )|(?<=&)function(?= )|(?<!.)function(?=\\()|(?<= )function(?=\\()|(?<=&)function(?=\\()|(?<=\\})display|(?<=\\{)display|(?<!.)display(?= )|(?<= )display(?= )|(?<=&)display(?= )|(?<!.)display(?=\\()|(?<= )display(?=\\()|(?<=&)display(?=\\()|(?<=\\})display|(?<=\\{)display|int |str |float|,|\{|\}|\(|\)|\n|;)'

    #Splits the data into its parts (USES THE REGEX)
    tokenized = re.split(splitby, data+"\n")
    
    #TOKENIZATION 
    output = []
    
    tokenized = [i for i in tokenized if i != None and i!=""]

    for token in tokenized:
        if token == ' ' or token == '': continue        
        if(token in keywords):
            output.append(["keyword", token])
        elif(token in equals):
            output.append(["equals", token])
        elif(token in newline):
            output.append(["newline", token])
        elif(token in operators):
            output.append(["operator", token])
        elif(token in separators) or token in newline:
            output.append(["separator", token])
        elif(token.replace(' ','').isnumeric()):
            output.append(["integer", token.replace(' ','')])
        else:
          output.append(["identifier", token])

    correct_output = []
    splits = [ ['newline', '\n'], ['newline', ';'], ['separator', '{'], ['separator', '}']]


    # SPLITS INTO LINES OF CODE

    current = [ ]
    #print(output)
    for i in output:
        
        if i in splits:
            if current != []:
                correct_output.append(current)
            
            if i[1] == '}' or i[1] == '{': 
                #print(100, i)
                correct_output.append([i])

        
            
            current = []
            
    
        else:

            current.append(i)
    
    correct_output.append(current)



    return correct_output