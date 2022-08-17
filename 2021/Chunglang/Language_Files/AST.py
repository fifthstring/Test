import re
operator_heirarchy = {
    4: '^',
    3 : '/',
    2 : '*',
    1 : '+',
    0 : '-'
}

z = list(operator_heirarchy.values())[::-1]

logic_heirarchy = {
    8 : '<=',
    7 : '>=',
    6 : '>',
    5 : '<',
    4 : '!=',
    3 : '==',
    2 : '|',
    1 : '&',
}

combined_heirarchy = {
    14 : 'j',
    13 : '^',
    12 : '/',
    11 : '*',
    10 : '+',
    9 : '-',
    8 : '<=',
    7 : '>=',
    6 : '>',
    5 : '<',
    4 : '!=',
    3 : '==',
    2 : '|',
    1 : '&',

}

l = list(logic_heirarchy.values())[::-1]

c = list(combined_heirarchy.values())[::-1]

def combined_AST(data):
    data = data.replace(" ","")
    
    if data.isnumeric() or data.isalpha() or data in (True, False):
        return Node(data)
    
    while '(' in data:
        index = data.index('(')
        close = Closing_Bracket(data, index)

        data = data[0:index] + str(evaluate_combined(combined_AST(data[index+1:close]))) + data[close+1:]

    operators = []

    for i in range(1, len(data)):
        
        if data[i] == '=' and data[i-1] in ('=', '<' ,'>', '!'):
            operators.append(c.index( str(data[i-1]+data[i])) )
        elif data[i] in c and data[i+1] != '=':
            operators.append(c.index(data[i]))

    operators = min(operators) + 1

    if len(combined_heirarchy[operators]) == 1:
        splitby = "\\" + combined_heirarchy[operators]+ '(?!=)'
        data = re.split(splitby, data)
        
    else:

        data = data.split(combined_heirarchy[operators])
        #exit()

    root = Node(combined_heirarchy[operators])


    for i in data:
        root.children.append(combined_AST(i))

    return root

def evaluate_combined(tree):
    
    op = tree.value
    #print(op)

    
    if op == 'True':
        return True
    elif op == 'False':
        return False
    elif op.isnumeric():
        return int(op)
    elif op.isnumeric() or op.isalpha() or op in (True, False):
        return op
    
    if op == '>':
        x=  [evaluate_combined(i) for i in tree.children]
        if x[0] > x[1] :
            return True
        return False
    
    if op == '>=':
        x=  [evaluate_combined(i) for i in tree.children]
        if x[0] >= x[1] :
            return True
        return False
    
    if op == '<':
        x=  [evaluate_combined(i) for i in tree.children]
        if x[0] < x[1] :
            return True
        return False
    
    if op == '<=':
        x=  [evaluate_combined(i) for i in tree.children]
        if x[0] <= x[1] :
            return True
        return False

    if op == '!=':
        x=  [evaluate_combined(i) for i in tree.children]
        if x[0] != x[1] :
            return True
        return False
    


    if op == '==':
        #print('RECOGNIZED')
        prev = None
        for i in [evaluate_combined(i) for i in tree.children]:
            if prev == None:
                prev = str(i)
            elif str(i) != prev:
                return False
        return True


   
        #return evaluate_operation_AST(tree.children[0]) * evaluate_operation_AST(tree.children[1])
    
    if op == '&':
    
        if [evaluate_combined(i) for i in tree.children].count(True) == len(tree.children):
            return True
        return False
    
    
    if op == '|':
        #print([evaluate_combined(i) for i in tree.children])
        if [evaluate_combined(i) for i in tree.children].count(True) >= 1:
            return True
        return False
    
    if op == '*':

        result = 1
        for x in tree.children:
            result *= evaluate_combined(x)

        return result
        #return evaluate_operation_AST(tree.children[0]) * evaluate_operation_AST(tree.children[1])
    
    if op == '/':
        result = ''
        for x in tree.children:
            if result == '': result = evaluate_combined(x)
            else: result /= evaluate_combined(x)

        return result
        #return evaluate_operation_AST(tree.children[0]) / evaluate_operation_AST(tree.children[1])
    
    if op == '-':
        result = ''
        for x in tree.children:
            if result == '': result = evaluate_combined(x)
            else: result -= evaluate_combined(x)

        return result
        #return evaluate_operation_AST(tree.children[0]) - evaluate_operation_AST(tree.children[1])

    if op == '+':
        result = 0
        for x in tree.children:
            result += evaluate_combined(x)

        return result


        #return evaluate_operation_AST(tree.children[0]) + evaluate_operation_AST(tree.children[1])

    if op == '^':
        result = 0
        for x in tree.children:
            result = evaluate_combined(x) * evaluate_combined(x)

        return result


def logic_AST(data):

    data = data.replace(" ","")
    
    if data.isnumeric() or data.isalpha() or data in (True, False):
        return Node(data)
    
    #print(data)
    #print(l)
    operators = min([l.index(i) for i in data if i in l] + [l.index(data[i] + data[i-1] ) for i in range(1, len(data)) if data[i] == '=' and data[i-1] in ('=', '<', '>', '!')]) + 1


    data = data.split(logic_heirarchy[operators])


    root = Node(logic_heirarchy[operators])


    for i in data:
        root.children.append(logic_AST(i))

    return root


def evaluate_logic_AST(tree):
    op = tree.value
    #print(op)

    
    if op == 'True':
        return True
    elif op == 'False':
        return False
    elif op.isnumeric() or op.isalpha() or op in (True, False):
        return op
    
    if op == '>':
        x =  [evaluate_logic_AST(i) for i in tree.children]
        if x[0] > x[1] :
            return True
        return False
    
    if op == '>=':
        x=  [evaluate_logic_AST(i) for i in tree.children]
        if x[0] >= x[1] :
            return True
        return False
    
    if op == '<':
        x=  [evaluate_logic_AST(i) for i in tree.children]
        if x[0] < x[1] :
            return True
        return False
    
    if op == '<=':
        x=  [evaluate_logic_AST(i) for i in tree.children]
        if x[0] <= x[1] :
            return True
        return False

    if op == '!=':
        x=  [evaluate_logic_AST(i) for i in tree.children]
        if x[0] != x[1] :
            return True
        return False
    


    if op == '==':
        #print('RECOGNIZED')
        prev = None
        for i in [evaluate_logic_AST(i) for i in tree.children]:
            if prev == None:
                prev = i
            elif i != prev:
                return False
        return True


   
        #return evaluate_operation_AST(tree.children[0]) * evaluate_operation_AST(tree.children[1])
    
    if op == '&':
    
        if [evaluate_logic_AST(i) for i in tree.children].count(True) == len(tree.children):
            return True
        return False
    
    
    if op == '|':
        #print([evaluate_logic_AST(i) for i in tree.children])
        if [evaluate_logic_AST(i) for i in tree.children].count(True) >= 1:
            return True
        return False

    




class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        


def Closing_Bracket(data, openPos):
    closePos = openPos
    counter = 1
    while (counter > 0):
        closePos += 1
        c = data[closePos]

        if (c == '('):
            counter+=1
        
        elif (c == ')'):
            counter-=1
        
    
    return closePos;


#print(Closing_Bracket('(a ()bc)',0))



    
def create_operation_AST(data):
    
    if data.isnumeric():
        return Node(data)
    
    #print(data)

    while '(' in data:
        index = data.index('(')
        close = Closing_Bracket(data, index)

        data = data[0:index] + str(evaluate_operation_AST(create_operation_AST(data[index+1:close]))) + data[close+1:]
        #print(data)

    operators = min([z.index(i) for i in data if i in ('^','+','-','/','*')])


    
    data = data.split(operator_heirarchy[operators])
    root = Node(operator_heirarchy[operators])


    for i in data:
            root.children.append(create_operation_AST(i))
    #root.children[0] = create_operation_AST(data[0])
    #root.children[1] = create_operation_AST(data[1])

    return root
    
def evaluate_operation_AST(tree):
    op = tree.value
    if op.isnumeric() == True:
        return int(op)

    if op == '*':

        result = 1
        for x in tree.children:
            result *= evaluate_operation_AST(x)

        return result
        #return evaluate_operation_AST(tree.children[0]) * evaluate_operation_AST(tree.children[1])
    
    if op == '/':
        result = ''
        for x in tree.children:
            if result == '': result = evaluate_operation_AST(x)
            else: result /= evaluate_operation_AST(x)

        return result
        #return evaluate_operation_AST(tree.children[0]) / evaluate_operation_AST(tree.children[1])
    
    if op == '-':
        result = ''
        for x in tree.children:
            if result == '': result = evaluate_operation_AST(x)
            else: result -= evaluate_operation_AST(x)

        return result
        #return evaluate_operation_AST(tree.children[0]) - evaluate_operation_AST(tree.children[1])

    if op == '+':
        result = 0
        for x in tree.children:
            result += evaluate_operation_AST(x)

        return result


        #return evaluate_operation_AST(tree.children[0]) + evaluate_operation_AST(tree.children[1])

    if op == '^':
        result = 0
        for x in tree.children:
            result = evaluate_operation_AST(x) * evaluate_operation_AST(x)

        return result



def printTree(node, level=0):
    if node != None :


        if len(node.children) == 0:
            print(' ' * 4 * level + '->', node.value)
        else:
            for i in range(len(node.children)):
                printTree(node.children[i], level + 1)
                #printTree(node.children[0], level + 1)

                if i != len(node.children) -1:
                    print(' ' * 8 * level + '->', node.value)



        #printTree(node.children[1], level + 1)
    
    else:
        print(node)