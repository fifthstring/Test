from Language_Files.aLexer import lexer
#import COLOURS
from Language_Files.AST import printTree, combined_AST, evaluate_combined


def Closing_Bracket(data, openPos):
    closePos = openPos
    counter = 1
    while (counter > 0):
        closePos += 1

        c = data[closePos][0][1]
        if (c == '{'):
            counter += 1

        elif (c == '}'):
            counter -= 1

    return closePos


def check_for_if(data):
    for i in range(len(data) - 1):
        if data[i][1] == "if":
            return i


def if_statement(condition, toRun):
    #TORUN IS 3D list
    if str(evaluate_combined(combined_AST(''.join([i[1] for i in convert_variables_to_values(condition)])))) == "True":

        #print(toRun, 66)
        execute_code(toRun)
    else:
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.condition = None
        self.children = []



'''
def program_tree(DATA, data, root):

    i = 0
    while True:
        node = Node(data[i])

        if i >= len(data) - 1:
            break
        

        
        if not data[i]: pass
        elif data[i][0][1] == 'if':
           

            node = Node(data[i])

            t = []
            for j in range(len(DATA)):
                if Closing_Bracket(DATA, i + 1)-1>= j >= i+2:            
                    t.append(DATA[j])

            for i in t:
                node.children.append(i)
            
           
            #
            #node.children root_function(t,t)
            
            #print(node.value)
            root.children.append(node)

            print(node.children)

            i += len(node.children)+2

        else:

            print(i,data)
            root.children.append(node)

        i += 1

    return [node,root]
'''

reee = Node(0)
def program_tree(data,current):
    #print("RAN should appear 2wice", data)
    line = 0
    while line < len(data):
        #REMOVE ALL TABS IN DATA
        if len(data) > 0:
            if len(data[line]) > 0:

                if data[line][0][1].strip() == "":
                        data[line].remove(data[line][0])
                        print("STRIPPED")

            if len(data[line]) > 0:
                if data[line][0][1] == 'if':
                    print("SUI")
                    newNode = Node([])
                    t = []
                    for j in range(len(data)):
                        if Closing_Bracket(data, line + 1)-1>= j >= line+2:            
                            t.append(data[j])
                    for i in t:
                        newNode.value.append(i)


                    #REMOVAL
                    toremove = newNode.value

                    opening = line
                    end = Closing_Bracket(data,line+1)+1
                    

                    data = data[:opening] + data[end:]

                    
                    current.children.append(newNode)

                    
                    program_tree(newNode.value, newNode)
                    line = 0

        line = line + 1
            
    
l = lexer()
reee.value = l
p = program_tree(l,reee)


def dfs(tree):
    print(tree.value)
    for i in tree.children:
        dfs(i)


#dfs(x)

#printTree(x)

colors = {
    'green': '\033[92m',
    'red': '\033[31m',
    'black': '\033[m',
    'end': '\033[0m'
}

#CHECKERS


def check_for_assignment(data):
    for i in range(len(data) - 1):
        if data[i][0] == "identifier" and data[
                i + 1][0] == "equals" and data[i + 2][0] != "equals":
            return i


def check_for_display(data):
    for i in range(len(data) - 1):
        if data[i][1] == "display":
            return i


def check_for_output(data):
    for i in range(len(data)):
        if data[i][0] == "keyword" and data[i + 1][0] == "seperator" and (
                data[i + 2][0] == "variable" or data[i + 2][0]
                == "identifier") and data[i + 3][0] == "seperator":
            return True
    return False


variables = {}


#does what it says on the tin
def identifier_to_variable(data):

    for i in range(len(data)):
        if data[i][1].replace(
                ' ', '') in variables.keys() and data[i][0] == 'identifier':
            data[i][0] = 'variable'
    #print(data)
    return data


#does what it says on the tin
def convert_variables_to_values(inp):
    for l in range(len(inp)):
        for i in variables.keys():
            if inp[l][1].replace(' ', '') == i:
                inp[l][0] = variables[i][0]
                inp[l][1] = variables[i][1]
    return inp


#ASSIGNMENT #INP is one line of data
def Assignment(inp, check):
    #Checks for operation
    #print(inp)

    if 'operator' in [i[0] for i in inp]:
        newvar = inp[check][1].replace(' ', '')
        toinput = inp[check + 2:]
        sped = str(
            evaluate_combined(
                combined_AST(''.join(
                    [i[1] for i in convert_variables_to_values(toinput)]))))
        if sped != 'True' and sped != 'False':
            variables[newvar] = ["integer", sped]
        else:
            variables[newvar] = ["Boolean", sped]
    else:
        variables[inp[check][1].replace(' ',
                                        '')] = ["string", inp[check + 2][1]]


#DISPLAY # INP IS ONE LINE OF DATA
def Display(inp, check):
    #print(inp, 88)
    varconvert = ""

    for i in inp[check + 1:]:
        varconvert = varconvert + (i[1])

    count = 0
    #CONVERTS VARIABLES
    for l in range(len(varconvert)):
        for i in variables.keys():
            if varconvert[l].replace(' ', '') == i:
                if "_" in varconvert[l - 1]:
                    #print("BRUH")
                    varconvert = [i for i in varconvert]
                    varconvert[l] = variables[i][1]
                    varconvert = ''.join(varconvert)
                    count += 1

    varconvert = [i for i in varconvert]
    for i in range(count):
        varconvert.remove('_')
    varconvert = ''.join(varconvert)
    parts = varconvert.split(",")

    todisplay = ""
    #DOES OPERATIONS

    #print(parts)
    for i in range(len(parts)):
        if len(parts[i]) > 1:

            for op in [
                    '>', '<', '<=', '>=', '!=', '==', '+', '-', '*', '/', '^'
            ]:
                if (op in [j[0] for j in parts[i]]):

                    beep = evaluate_combined(combined_AST(" ".join(parts[i])))
                    todisplay = todisplay + str(beep)

                    break

            else:

                todisplay += parts[i]

    print(colors['green'] + "OUTPUT:" + colors['black'] + todisplay)


#THE DATA

data = lexer('input.txt')
counter = 0


def execute_code(i):

    #print(i , 99999999)
    check = check_for_assignment(i)
    check2 = check_for_display(i)
    if str(check).isnumeric():
        Assignment(i, check)
    if str(check2).isnumeric():

        Display(i, check2)
    
    #if str(check3).isnumeric():
        #if_statement(i, check3)


if data.count(['separator', '{']) != data.count([
        'separator', '}'
]) or data.count(['separator', '(']) != data.count(['separator', ')']):
    print(colors['red'] + "__________________________________\n\n" +
          '\nSyntax Error\n' + " " + '\nInvalid Syntax\n' +
          '\nBRACKET PAIR NOT COMPLETE\n' +
          "\n__________________________________\n")
    exit()


root = Node(0)

for i in root.children:
    #print(i.value, 'iter')

    #execute_code(i.value)

    
    check = check_for_assignment(i.value)
    check2 = check_for_display(i.value)
    check3 = check_for_if(i.value)
    #print(check, check2, check3)
    if str(check).isnumeric():
        Assignment(i.value, check)
    elif str(check2).isnumeric():
        Display(i.value, check2)
    elif str(check3).isnumeric():
        if_statement(i.value[1:], i.children[0].value)