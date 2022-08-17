#numeral = input('Enter numeral')
nums = [1,4,5,9,10,40,50,90,100,400,500,1000]
letters = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','M']
nums.reverse()
letters.reverse()
vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
c = {}
def number_to_numeral(h):
    output = ''
    count=-1
    while True:
        count += 1
        if count>len(nums):
            count=0
        if h>=nums[count]:
            output += letters[count]
            h -= nums[count]
            count = 0
        if h==0:
            break
    return output
  
def split(n):
    split = [0]
    current = ''
    for i in range(len(n)):
        if n[i] != current:
            split.append(i)
        current=n[i]
    sep=[]
    for i in range(len(split)-1):
        sep.append(n[split[i]:split[i+1]])
    sep.append(n[split[-1]:])
    sep = [i for i in sep if i!='']

    for i in range(0,len(sep)-1,2):
        c[sep[i+1]] = sep[i]
    
    return sep


b= input('Enter numerals')
b=split(b)
def replace(n):
    output = ''
    for i in n:
        #print(len(i))
        output += number_to_numeral(len(i)) + i[0]

    return output

n=int(input('Enter n'))
for i in range(n-1):
    b = replace(b)
    b = split(b)
b=replace(b)
print(b.count('I'),b.count('V'))

