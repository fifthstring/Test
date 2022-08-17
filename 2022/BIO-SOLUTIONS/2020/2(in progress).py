plan = 'FEDC'
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[0:len(plan)+2])
connections = {i:[] for i in alphabet}

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
to_add = ''
for letter in plan:
    alphabet = alph[0:len(plan)+2] + to_add
    alphabet = [i for i in alphabet if i not in plan]
    connections[alphabet[0]].append(letter)

    alph = alph.replace(alphabet[0],'')
    to_add += alphabet[0]
    plan = plan[1:]

none = [key for key in connections.keys() if connections[key] == []]


connections[none[0]].append(none[1])

for key in connections.keys():
    k = connections[key]
    for room in k:
        if key not in connections[room]:
            connections[room].append(key)


for k in connections.keys():
    connections[k] = sorted(connections[k])
    print(connections[k])

plan = 'FEDC'

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[0:len(plan)+2])
print(alphabet)
count = {i:[0,1] for i in alphabet}
count['A'] = [1,1]
start_room = 'A'
n = 876543
for i in range(n):

    
    if count[start_room][0] % 2 != 0:
        end_room = connections[start_room][0]
    else:

        if len(connections[start_room]) >= 2:
            end_room = connections[start_room][count[start_room][1]]
        else:
            end_room = connections[start_room][0]



        count[start_room][1] += 1
        if count[start_room][1] >= len(connections[start_room]) :
            
            count[start_room][1] = 1



    
    count[start_room][0] += 1
    start_room = end_room


print(end_room)