'''
Question 1: Down Pat
A pat is a single letter or a string of letters which can be split into a left and right string (of at least 1 letter)
where: each is the reverse of a pat; and all the letters in the left string are later in the alphabet than all the
letters in the right string.
For example:
• BA is a pat as it splits into B and A, both of which are single letters and therefore pats, and B is
alphabetically after A. AB is not a pat as the alphabetical rule would be broken;
• Similarly ED is a pat but DE is not;
• DEC is a pat as it splits into DE (whose reverse ED is a pat) and C.
• CEDAB splits into CED and AB, whose reverses are pats and C, E, and D are after A and B
alphabetically.
'''

s1, s2 = input().split(' ')

def output(i):
    if i == True:
        return 'YES'
    
    else:
        return 'NO'

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

print(output(recursive_pat(s1)))
print(output(recursive_pat(s2)))
print(output(recursive_pat(s1+s2)))
