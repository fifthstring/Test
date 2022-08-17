#challenge 1
'''
answer = 0
for x in range(1000):
  if x % 3 == 0 or x%5 == 0:
    answer += x
  
  
print(answer)
'''

#challenge 2
'''
num = [1,1]

p1 = 0
p2 = 1
count = 0
for x in range (1,100000):
  ans = num[p1] + num[p2]
  if ans < 4000000:
    num.append(ans)
    p1 += 1
    p2 += 1
    if ans%2 ==0:
      count += ans
print(num)
print(count)
'''
#challenge 3
'''

n = 600851475143
primes_in_n = []
for x in range(10000):
  if x >1:
    for y in range(2,x):
      if x % y == 0:
        break
      else:
        if n % x == 0:


          primes_in_n.append(x)

lenn = len(primes_in_n)
print(primes_in_n[lenn-1])


#nump = x % y
#if n % nump == 0:
'''
#challenge 4 - INCOMPLETE
'''
h1 = 100
h2 = 100
hundreds = []
for x in range(100000,998001):
  string = str(x)
  if(string[0] == string[5]):
    if(string[1] == string[4]):
      if(string[2] == string[3]):
        while h1 < 1000:
          for x in range(100):
            h1 += 1
            for x in range(100):
              h2 += 1
              hundreds.append(str(h1*h2))
          if string in hundreds:
            print(string)
'''

#challenge 5
'''
possible_chance = True
big = []
for x in range(1000):
  possible_chance = True
  for y in range(1,20):
    count = 0
    while count < 20:
      count += 1
      if x % y != 0:
        possible_chance = False
    
    if possible_chance == True:
      big.append(x)
      

print(big)
'''
'''
check_list = [11, 13, 14, 16, 17, 18, 19, 20]
                                              
def find_solution(step):
    for x in range(step, 999999999, step):
        if all(x % n == 0 for n in check_list):
            return x
    return None
    
if __name__ == '__main__':
    solution = find_solution(2520)
    if solution is None:
        print ("No answer found")
    else:
        print ("found an answer:", solution)
'''
# Challenge 6

'''
count = 1
count2 = 1

for x in range(1,101):#
  count += x^2
  count2 += x
  

print(count - count2^2)
'''



print(eval(input('SUM?')))

