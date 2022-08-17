import re

math_and_logic_heirarchy = {
    14: '%',
    13: '^',
    12: '/',
    11: '*',
    10: '-',
    9: '+',
    8: '<=',
    7: '>=',
    6: '>',
    5: '<',
    4: '!=',
    3: '==',
    2: '|',
    1: '&',
}

c = list(math_and_logic_heirarchy.values())[::-1]


valid_tokens = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.?!#@;:_'


def math_and_logic_AST(data):
    
    i=0
 
    data = data.lstrip()
    data = [ i for i in data]
    while i < len(data):
        
        if data[i] == ' ':

            if data[i-1] not in valid_tokens:
                data.pop(i)
                i -= 1

            elif i+1<len(data):
                if data[i+1] not in valid_tokens:
                    data.pop(i)
                    i -= 1


            
        i+=1

    data = ''.join(data)
    print(data)


    if data.isnumeric() or data.isalpha() or data in (True, False) or (False not in [i in valid_tokens for i in data.replace(' ', '')]):

        return Node(data)
  

    while '(' in data:
        index = data.index('(')
        close = Closing_Bracket(data, index)
        data = data[0:index] + str(
            evaluate_math_and_logic_AST(math_and_logic_AST(
                data[index + 1:close]))) + data[close + 1:]



    operators = []

    for i in range(1, len(data)):
        if data[i] == '=' and data[i - 1] in ('=', '<', '>', '!'):
            operators.append(c.index(str(data[i - 1] + data[i])))
        elif data[i] in c and data[i + 1] != '=':
            operators.append(c.index(data[i]))


    try:
        operators = min(operators) + 1
    except:
        return Node(data)




    if len(math_and_logic_heirarchy[operators]) == 1:
        splitby = "\\" + math_and_logic_heirarchy[operators] + '(?!=)'
        data = re.split(splitby, data)
    else:
        data = data.split(math_and_logic_heirarchy[operators])

        
    root = Node(math_and_logic_heirarchy[operators])

    for i in data:
        root.child_nodes.append(math_and_logic_AST(i))

    return root



def evaluate_math_and_logic_AST(tree):

    
    op = tree.value
    

    if op == 'True':
        return True
    elif op == 'False':
        return False
    elif op.isnumeric():
        return int(op)
    elif op.replace('.','').isnumeric():
        return int(float(op))
    elif op.isnumeric() or op.isalpha() or op in (True, False):
        return op
    elif False not in [i in valid_tokens for i in op.replace(' ', '')]:
        return op
    



    if op == '>':
        x = [evaluate_math_and_logic_AST(i) for i in tree.child_nodes]
        if x[0] > x[1]:
            return True
        return False

    if op == '>=':
        x = [evaluate_math_and_logic_AST(i) for i in tree.child_nodes]
        if x[0] >= x[1]:
            return True
        return False

    if op == '<':
        x = [evaluate_math_and_logic_AST(i) for i in tree.child_nodes]
        if x[0] < x[1]:
            return True
        return False

    if op == '<=':
        x = [evaluate_math_and_logic_AST(i) for i in tree.child_nodes]
        if x[0] <= x[1]:
            return True
        return False

    if op == '!=':
        x = [evaluate_math_and_logic_AST(i) for i in tree.child_nodes]
        if x[0] != x[1]:
            return True
        return False

    if op == '==':
        prev = None
        for i in [evaluate_math_and_logic_AST(i) for i in tree.child_nodes]:
            if prev == None:
                prev = str(i)
            elif str(i) != prev:
                return False
        return True

    if op == '&':
        y = [evaluate_math_and_logic_AST(i) for i in tree.child_nodes
            ]
        if y.count(True) == len(y):
            return True
        return False

    if op == '|':
        if [evaluate_math_and_logic_AST(i) for i in tree.child_nodes].count(True) >= 1:
            return True
        return False

    if op == '%':
        result = ''
        for x in tree.child_nodes:
            if result == '': result = evaluate_math_and_logic_AST(x)
            else: result %= evaluate_math_and_logic_AST(x)

        return result

    if op == '*':

        e = [str(evaluate_math_and_logic_AST(i)) for i in tree.child_nodes]

        if not e[0].replace('.','').isnumeric():
            result = e[0]
            for x in range(1,len(tree.child_nodes)):
                result *= evaluate_math_and_logic_AST(tree.child_nodes[x])
        else:
            result = 1
            for x in tree.child_nodes:
                result *= evaluate_math_and_logic_AST(x)

        return result

    if op == '/':
        result = ''
        for x in tree.child_nodes:

            if result == '': result = int(evaluate_math_and_logic_AST(x))
        
            else: result /= int(evaluate_math_and_logic_AST(x))

        return result

    if op == '-':
        result = ''
        for x in tree.child_nodes:
            if result == '': result = int(evaluate_math_and_logic_AST(x))
            else: result -= int(evaluate_math_and_logic_AST(x))

        return result

    if op == '+':

        
        e = [ str(evaluate_math_and_logic_AST(i)) for i in tree.child_nodes]

        #print([i.replace(' ','').isnumeric() or i.replace('.', '').isnumeric() for i in e])
        if False not in [i.replace(' ','').isnumeric() or i.replace('.', '').isnumeric() for i in e]:
            result = 0
        
        else:
            result = ''

        
        for x in tree.child_nodes:
            result += (evaluate_math_and_logic_AST(x))

        return result

    if op == '^':
        result = 0
        result = int(evaluate_math_and_logic_AST(tree.child_nodes[0])) ** int(evaluate_math_and_logic_AST(tree.child_nodes[1]))

        return result


class Node:
    def __init__(self, value):
        self.value = value
        self.child_nodes = []


def Closing_Bracket(data, openPos):
    
    closePos = openPos
    counter = 1
    while (counter > 0):
        closePos += 1
        c = data[closePos]

        if (c == '('):
            counter += 1

        elif (c == ')'):
            counter -= 1

    return closePos



def printTree(node, level=0):
    if node.child_nodes:
        for i in node.child_nodes:
            print(('   '*level*2),i.value)
            printTree(i, level+1)

    
    
    