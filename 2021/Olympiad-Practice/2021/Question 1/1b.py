import itertools

abcd = list(itertools.permutations('ABCD'))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def recursive_pat(pat):
    if len(pat) == 1:
        return True

    for i in range(1,len(pat)):#

        strings = [pat[:i][::-1], pat[i:][::-1]]
        lowest_left = alphabet.index(min(strings[0]))
        highest_right = alphabet.index(max(strings[1]))
        if lowest_left < highest_right:
            continue
        else:
            return recursive_pat(strings[0]) and recursive_pat(strings[1])
    else:
        return False

pats = []

for i in abcd:
    if recursive_pat(i):
        pats.append(i)