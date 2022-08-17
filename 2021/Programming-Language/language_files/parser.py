functions = ['upper', 'lower', 'input']


class Node:
    def __init__(self, val=0):
        self.value = val
        self.else_run = []
        self.child_nodes = []

   
    def execute(self):
        pass


def Closing_Bracket(data, openPos):
    closePos = openPos
    counter = 1
    while (counter > 0):
        closePos += 1
        try:
            c = data[closePos][1]
            if type(c) == str:
                c=c.replace(' ', '')
        except: ''
        if (c == '{'):
            counter += 1

        elif (c == '}'):
            counter -= 1

    return closePos

def generate_syntax_tree(data, current_parent=Node(0)):
    i=0
    flag=0
    i = len(data) - 1


    while True:
        if i <= -1:
            break
        if data[i][1] == 'input':
            y = [['input', data[i + 1]]]
            data = data[0:i] + y + data[i + 2:]
            i = len(data) - 1
        elif data[i][1] == 'upper':
            y = [['upper'] + [i for i in data[i + 1]]]
            data = data[0:i] + y + data[i + 2:]

            i = len(data) - 1

        i -= 1

    
    i = len(data) - 1
    while True:
        if i <= -1:
            if flag == 0:
                break
            else:
                i = len(data) - 1
                flag=0


        if data[i][0] == 'operator' or data[i][0] == 'operation':
            if (data[i - 1][0] in ('string', 'integer', 'variable', 'operation', 'lower', 'upper')
                ) and (data[i + 1][0] in ('string', 'integer', 'variable', 'operation', 'lower', 'upper')):


                
                y = [['operation', [ [data[i - 1]] + [data[i]] +  [data[i + 1]]]]]

                data = data[0:i - 1] + y + data[i + 2:]
                i = len(data) - 1


                flag=1

        i-=1  
       


        


    

    
    
    
    
    i = -1 

    #exit()



    #exit()

    while True:

        if len(data) - 1 <= i:
            break

        i += 1

        if data[i][1] == 'display' and data[i + 1][0]:
            node = Node(['display', data[i + 1]])
            current_parent.child_nodes.append(node)


        if data[i][1] == 'delay':
            node = Node(['delay', data[i+1]])
            current_parent.child_nodes.append(node)

    
        if data[i][1] == 'break':
            #print('Found Break')
            node = Node(['break', 0])
            current_parent.child_nodes.append(node)
        if data[i][0] == 'assignment':
            node = Node(['variable', [data[i - 1][1], data[i + 1]]])
            current_parent.child_nodes.append(node)

        if data[i][1] == 'loop':
            node = Node(['loop', data[i + 1][1]])
            end = Closing_Bracket(data, i+3)
            to_run = data[i + 3: end]
            node.child_nodes = generate_syntax_tree(
                to_run, Node(['loop', data[i + 1][1]])).child_nodes

            current_parent.child_nodes.append(node)
            i += 2 + len(to_run)

        if data[i][1] == 'if':
            node = Node(['if', data[i + 1][1]])
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

    return current_parent
