parameters = {
    'upper': [['string', 'function', 'operation','variable', 'operator']],
    'lower': [['string', 'function', 'operation','variable', 'operator']],
    'input': [['string', 'function', 'operation','float','integer','variable', 'operator']],   
    'length': [['string', 'variable', 'function']] 
}

def bracket_removal(d):
    while len(d) == 1:
        d = d[0]


    return d


def c(i):

    while len(i ) == 1:
        i = i[0]

    return i
def join(data, out=[]):
    i=len(data) - 1

    while i >= 0:
        
        #print(c(data[i]))
        if data[i][0] in ('variable','integer', 'operator', 'operation', 'function', 'string') or c(data[i])[0] in ('integer', 'operator', 'operation', 'function', 'string'):
            if i + 1 < len(data):
                if data[i+1][0] in ('integer', 'operator', 'operation', 'function', 'string')or c(data[i+1])[0] in ('integer', 'operator', 'operation', 'function', 'string'):
                    data[i] = data[i] + data[i+1] 
                    data.pop(i+1)
                    i = i + 1

    
        else:
            out.append(data[i])
                    

            
        i -= 1


    return data



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



def parse(data, out=[]):
    i = 0




    while len(data) == 1:
        data = data[0]
    while i  < len(data):

        if data[i][0] == 'paren' and '(' in data[i][1]:

            end = closing_paren(data, i + 1)
            within = data[i+1:end+1]
            data[i] += join(parse(within, [])) 

            for j in range(len(within) + 2):
                data.pop(i+1)
                

            out.append(data[i])

            i += len(within)

    

        else:

            if data[i][0] != 'paren' and ')' not in data[i][1]:
                if data[i][0] == 'function':
                    end = closing_paren(data, i + 1)
                    within = data[i+2:end+1]
                    data[i] += join(parse(within, []))

                    for j in range(len(within) + 2):
                        data.pop(i+1)
                

                    

                out.append(data[i])

        i+= 1


    return join(out)

            


class Node:
    def __init__(self, val=0):
        self.value = val
        self.else_run = []
        self.child_nodes = []


 
def Closing_Bracket(data, openPos):
    closePos = openPos
    counter = 1
    while (counter > 0):
        closePos += 1
        c = data[closePos][1]
        if type(c) == str:
            c=c.replace(' ', '')
        
        if (c == '{'):
            counter += 1

        elif (c == '}'):
            counter -= 1

    return closePos



def generate_syntax_tree(data,current_parent=Node(0)):
    i = 0

    while True:

        if len(data) - 1 <= i:
            break
        

        if data[i][1] == 'display' and data[i + 1][0]:
            node = Node(['display', data[i + 1]])
            current_parent.child_nodes.append(node)


        if data[i][1] == 'delay':
            node = Node(['delay', data[i+1]])
            current_parent.child_nodes.append(node)

    
        if data[i][1] == 'break':
            node = Node(['break', 0])
            current_parent.child_nodes.append(node)
        if data[i][0] == 'assignment':
            node = Node(['variable', [data[i - 1][1], data[i + 1]]])
            current_parent.child_nodes.append(node)

        if data[i][1] == 'loop':
            node = Node(['loop', data[i + 1]])

            
            end = Closing_Bracket(data, i+3)

            to_run = data[i + 3: end]
            
            node.child_nodes = generate_syntax_tree(
                to_run, Node(['loop', data[i + 1][1]])).child_nodes

            current_parent.child_nodes.append(node)
            i += 2 + len(to_run)

        if data[i][1] == 'if':
            node = Node(['if', data[i + 1]])


            end = Closing_Bracket(data, i + 3)
            to_run = data[i + 3:end]


            if len(data) > end + 1:
                if data[end + 1][1] == 'else':
                    else1 = end + 3
                    else2 = Closing_Bracket(data, else1)
                    else_run = data[else1:else2]

                    i += 2 + len(else_run)
                    node.else_run = generate_syntax_tree(
                        else_run, Node(['if', data[i + 1][1]])).child_nodes

            node.child_nodes = generate_syntax_tree(
                to_run, Node(['if', data[i + 1][1]])).child_nodes

            current_parent.child_nodes.append(node)
            i += 2 + len(to_run)
        

        i += 1





                    
    return current_parent



def printTree(node, level=0):
    if node.child_nodes:
        for i in node.child_nodes:
            print(('   '*level*2),i.value)
            printTree(i, level+1)
        
    if node.else_run:
        print('   '*(level-1)*2, ['else'])
        for i in node.else_run:
            print(('   '*level*2),i.value)
            printTree(i, level+1)



