'''2020 British Informatics Olympiad Round One exam
Question 1: Roman Look-and-Say
The Roman look-and-say description of a string (of Is, Vs, Xs, Ls, Cs, Ds and Ms) is made by taking each
block of adjacent identical letters and replacing it with the number of occurrences of that letter, given in
Roman numerals (*), followed by the letter itself. A block of adjacent identical letters is never broken
into smaller pieces before describing it.
For example:
• MMXX is described as “two Ms followed by two Xs”. Since two is II in Roman numerals, this is
written as IIMIIX;
• IIMIIX is described as IIIIMIIIIX, which is “two Is, one M, two Is, one X”;
• IIIIMIIIIX is described as IVIIMIVIIX;
• It is not valid to describe III as, “two Is, one I” IIIII.
Note that Roman look-and-say descriptions are not necessarily Roman numerals.'''


def break_apart(s):

    out = []
    current = ''

    for letter in s:
        if current == '':
            current += letter

        elif current[-1] == letter:
            current += letter

        else:
            out.append(current)
            current = letter

    out.append(current)
    return out



def num_to_numeral(n):
    numerals = {
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1
    }
    out = ''

    while n > 0:
        for key, value in numerals.items():
            if n >= value:
                n -= value
                out += key
                break

    return out
        
        



n = 'MMDCCCLXXXVIII'
for i in range(50):
    x = break_apart(n)
    out = []
    for grouping in x:
        out.append(num_to_numeral(len(grouping)) + grouping[0])

    n = ''.join(out)


print(n.count('I'), n.count('V'))
