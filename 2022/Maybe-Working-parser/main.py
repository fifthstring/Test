from lexer import lex
import sys
from parser import printTree, generate_syntax_tree, parse
from trees import evaluate_math_and_logic_AST, math_and_logic_AST


#print(parse(lex()))

variables = {}

def vals_to_vars(string):
    if type(string) == str:
        string = string.split(' ')
        string = [ str(variables[i[1:]]) if i[1:] in variables.keys() and i[0] == '_' else i for i in string]
        return ' '.join(string)
    return string



def convert_list(l):
    
    l = [ '(' + convert_list(i) + ')' if type(i) == list else i for i in l]
    l = ''.join(l)
    return l



def evaluate_list(l):
    output = []

    if type(l) == list:
        while len(l) == 1:
            l = l[0]

    for i in range(len(l)):


        if type(l[i]) != list:

            if l[i] == 'function':
                if l[i+1] == 'input':


                    if type(l[i+2]) == list:
                        print(l[i+2])
                        x = evaluate_list(l[i+2])

                        output.append(input(evaluate_math_and_logic_AST(math_and_logic_AST(convert_list(x[0])))))
                    else:
                        output.append(input(l[i+3]))


                if l[i+1] == 'lower':

                    if type(l[i+2]) == list:
                        x = evaluate_list(l[i+2])
                        output.append(x[0].lower())
                    else:
                        output.append(l[i+3].lower())


                if l[i+1] == 'upper':

                    if type(l[i+2]) == list:
                        x = evaluate_list(l[i+2])
                        output.append(x[0].upper())
                    else:
                        output.append(l[i+3].upper())

                



                


            elif l[i] == 'operator':
                output.append(l[i+1])

            elif (l[i] == 'integer' or l[i] == 'string') :
                if l[i-1] != 'input' and l[i-2] != 'function':
                    #print(l, 77)
                    #print('pendin', l[i+1])
                    output.append(l[i+1])


            elif l[i] == 'variable':
                output.append(str(variables[l[i+1]]))


        else:

            if i - 2 >= 0 and l[i-2] == 'function':
                pass
            else:
                output.append(evaluate_list(l[i]))


    return output






def interpret_AST(node):

    if node.value:
        

        if node.value[0] == 'variable':
            variables[node.value[1][0]] = vals_to_vars(evaluate_math_and_logic_AST(math_and_logic_AST(convert_list(evaluate_list(node.value[1][1])))))
        if node.value[0] == 'display':

            
            print(vals_to_vars(evaluate_math_and_logic_AST(math_and_logic_AST(convert_list(evaluate_list(node.value[1]))))))


        if node.child_nodes and node.value:
            if node.value[0] == 'if':
                condition = node.value[1:]
                #print(condition)
                answer = evaluate_math_and_logic_AST(math_and_logic_AST(convert_list(evaluate_list(condition))))
                
                if answer == True:
                    for i in node.child_nodes:
                        interpret_AST(i)
                
                else:

                    if node.else_run:

                        for i in node.else_run:
                            interpret_AST(i)


            
            if node.value[0] == 'loop':
                n = node.value[1:]
                answer =str(evaluate_math_and_logic_AST(math_and_logic_AST(convert_list(evaluate_list(n)))))
                
                if answer.isnumeric():
                    for i in range(int(answer)):
                        for i in node.child_nodes:
                            interpret_AST(i)


                elif answer == 'True' or answer == 'False':
                    while evaluate_math_and_logic_AST(math_and_logic_AST(convert_list(evaluate_list(n)))):
                        for i in node.child_nodes:
                            interpret_AST(i)
                
                else:
                    print(answer)

                



               
            
    else:
        for i in node.child_nodes:
            interpret_AST(i)

syntax_tree = parse(lex())
#print(syntax_tree)
s = syntax_tree
syntax_tree = generate_syntax_tree(syntax_tree)
interpret_AST(syntax_tree)


