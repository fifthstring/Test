from Language_Files.aLexer import lexer 
cool = lexer()

colors = {
    'green' : '\033[92m',
    'red' : '\033[31m',
    '69' : '\033[89m',
    'black' : '\033[m',
    'end' : '\033[0m'
}
end = "\033["
output= ""
for l in cool:
    for i in range(len(l)):
        if l[i][0] == "keyword":
            output = output + (colors['green']+l[i][1] +end)
        elif l[i][0] == "operator":
            output = output+(colors['red']+l[i][1] +end)
        elif l[i][0] == "separator":
            output= output+(colors['69'] + l[i][1] +end)
        elif l[i][0] == "integer":
            output= output+(colors['end'] + l[i][1]+end)
        else:
            output = output+(colors['black'] + l[i][1]+end)
    output = output + "\n"

print(output)