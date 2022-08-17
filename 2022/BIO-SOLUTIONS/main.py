p = 2
q = 3
r = 10
s = 499
r -= 1
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:p]

solutions = []

level = [i for i in alphabet]

new_level = []
for i in range(r):
    for node in level:
        v = 1
        if len(node) >= q:
            check = node[-1*q:]
            
            for letter in alphabet:
                if not(check.count(check[0]) == len(check) and letter == check[0]):
                    new_level.append(node+letter)

                v = 0
        
        if v:
            for letter in alphabet:
                new_level.append(node + letter)


    

    level = new_level
    new_level = []


print(level[s])