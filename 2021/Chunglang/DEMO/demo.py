import re, sys

variables = {
'cheese': 'parmesan',
'nice': 'NICE!'}


def lexer(fp='input.txt'):

    keywords = [
    "else ",
    "if ",
    "while ",
    "return ",
    "function ",
    'display ',
    ]
    literals = [
        "int ",
        "str ",
        "float ",
    ]
    separators = [
        '\{',
        '\}',
        '\(',
        '\)',
        '&'
    ]
    operators = [
        '+',
        '-',
        '<',
        '==',
        '<=',
        '>=',
        "*",
        '/'
    ]
    equals = [
        "="
    ]
    newline = [
        "\\n"
    ]

    data = open(fp).read()
    
    #The thing that defines the split
    splitby = '(\=|\+|\-|\*'+ "|" + "|".join(keywords)+ "|" + "|".join(literals)+ "|" + "|".join(separators) + "|" + "|".join(newline) + ")"

    #Splits the data into its parts
    tokenized = re.split(splitby, data)

   #Gives each part a tag
    output = []
    for token in tokenized:
        if token == '' or token == '': continue        
        if(token in keywords):
            output.append(["keyword", token])
        elif(token in literals):
            output.append(["literals", token])
        elif(token in equals):
            output.append(["equals", token])
        elif(token in newline):
            output.append(["newline", token])
        elif(token in operators):
            output.append(["operator", token])
        elif(token in separators) or token == '\n':
            output.append(["separator", token])
        elif(token.isnumeric()):
            output.append(["integer", token])
        else:
          output.append(["identifier", token])
    return(output)

#Turns identifiers into variables
def identifier_to_variable(data):

    for i in range(len(data)):
        if data[i][1].lstrip() in variables.keys() and data[i][0] == 'identifier':
            data[i][0] = 'variable'
    return data

def parser(enter): 
    
    # two keywords in a row
    # identifier has to be followed by an operator or preceded by a keyword or followed by a separator

    # identifier + operator + (identifier or integer) [variable definition]
    # keyword==if + (variable or integer or identifier) + operator + (variable or integer or identifier)  [if statement]
    # keyword==print + (variable or integer or identifier) 


    commands = {
        "display" : print,
        "enter" : input, 
    }
    
    ##check all here
    lines = 0
    
    for i in range(len(enter)):
        

        # FUN DEMO THING (WILL MAKE AST LATER)


        if enter[i][0] == 'separator':
            enter = identifier_to_variable(enter)
            lines += 1

            
        elif enter[i][0] == 'keyword':
            if 'display' in enter[i][1]:
                print(enter[i+1])
                if enter[i+1][0] == 'variable':
                    output = variables[enter[i+1][1]]
                    print(output)
                elif enter[i+1][0] == 'integer' or enter[i+1][0] == 'identifier':
                    print(enter[i+1][1])
            
            enter = identifier_to_variable(enter)

        
        elif enter[i][0] == 'identifier' or enter[i][0] == 'variable':
            pass
        
        else:
            print(enter[i])
            sys.exit("_________________\n\n"+'Word ' + str(i) + ': ' + enter[i][1] + '\nSyntax Error\n' + "\n_________________")
            


        '''
        if enter[i-2][0] == "keyword" and enter [i-1][0] == "keyword":
            sys.exit('Line ' + str(i+1) + '\nSyntax Error\n' +" " + enter[i][1] + enter[i+1][1] + '\nCannot have two keywords in a row\n')
        if enter[i-1][0] == 'identifier' and (enter[i-2] != "keyword") and (enter[i] != "operator" or enter[i] != "seperator"):
            sys.exit('Line ' + str(i+1) + '\nSyntax Error\n' +" " + enter[i][1] + enter[i+1][1] + '\nInvalid Identifier\n')
        '''
def run():
        
    parser(lexer())

run()