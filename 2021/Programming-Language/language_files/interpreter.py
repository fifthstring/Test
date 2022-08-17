import re
variables = {}
from language_files.trees import evaluate_math_and_logic_AST, math_and_logic_AST
import time
def vals_to_vars(text):

    if type(text) == bool:
        return text
    
    res = re.split('(\W+)', text)    
    text = res
    text = [variables[i[1:]] if i[1:] in variables.keys() and i[0]=='_' else i for i in text 
    ]
    text = [str(i) for i in text]
    text = ''.join(text)
    return text


def display(value):



    if type(value) != list:
        return value


    if value[0] == 'string' or value[0] == 'integer':

        return vals_to_vars(value[1])


    elif value[0] == 'operation':
       
        

        e = []

        #print(value)

        if type(value[1]) == list:
            l = value[1][0]
            for i in l:
                #print(display(i))
                e.append(vals_to_vars(display(i)))


            e = ''.join(e)
            e = str(evaluate_math_and_logic_AST(math_and_logic_AST(e)))
            return e
        else:
            l = value[1]
            l = str(evaluate_math_and_logic_AST(math_and_logic_AST(vals_to_vars(l))))
            return l
        exit()









    elif value[0] == 'input':
        return input(display(value[1]))

    elif value[0] == 'upper':
        return display(value[2]).upper()

    else:

        return value[1]



def traverse_syntax_tree(node, level=0):

    if node.value:
        if node.value[0] == 'display':
            print(display(node.value[1:][0]))

        if node.value[0] == 'delay':
            time.sleep(int(node.value[1][1]) / 1000)
        
        
        if node.value[0] == 'variable':
        
            variables[node.value[1][0]] = display(node.value[1][1])
            

        if node.value[0] == 'break':
            return True

    if not node.child_nodes: return

    if node.value:
        br = False
        if node.value[0] == 'loop':
            for i in range(int(vals_to_vars(node.value[1]))):
                for i in node.child_nodes:
                    if br == True:
                        break
                    if traverse_syntax_tree(i, level + 1) == True:
                        br = True
                        break
                if br == True:
                    break
            

        if node.value[0] == 'if':


            print( display(['operation',node.value[1]]), '79797')
            if display(['operation',node.value[1]]):

                for i in node.child_nodes:
                    if traverse_syntax_tree(i, level + 1):
                        return True
            else:
                if node.else_run:

                    for i in node.else_run:

                        traverse_syntax_tree(i, level + 1)

    else:
        for i in node.child_nodes:
            traverse_syntax_tree(i, level + 1)
