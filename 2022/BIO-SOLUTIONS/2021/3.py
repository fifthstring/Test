to_add = list('ABCDEFGH')
target = 'AHGEFDCB'

def add(window):
    window= window + to_add[len(window)]
    return window

def rotate(window):
    m = window[0]
    window = window[1:] + m
    return window

def swap(window):
    w1 = window[1]
    w2 = window[0]
    window = window[2:]
    new_window = w1 + w2 + window
    return new_window

found_states = set()

def organize(boxes):
    count = 0
    while len(boxes) < 2:
        count += 1
        boxes = add(boxes)
        if boxes == target: return count

    count += 1
    level = [swap(boxes)]
    if len(to_add) > 0:
        level.append(add(boxes))

    if target in level: return count
        

    while True:
        count += 1
        new_level = []
    
        
        for i in level:  
            x = [swap(i), rotate(i)]
            if len(i) < len(target):
                x.append(add(i))
    
            for j in x:
                if j == target: 
                    return count
                
                elif j not in found_states:
                    new_level.append(j)
                    found_states.add(j)
    
            
        level = new_level[:]



print(organize(''))

