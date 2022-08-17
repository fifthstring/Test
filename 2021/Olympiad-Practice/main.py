'''
Input

The first line of the input contains a single integer T
(1≤T≤100

), denoting the number of test cases.

The first line of each test case contains three integers n,m,k
(1≤n≤104, 1≤m≤2×104, 1≤k≤8

), denoting the number of rooms, secret paths, and crewmates respectively.

Each of the next m
lines contains three integers u,v,w (1≤u, v≤n, u≠v, 1≤w≤104), denoting there is a secret path connecting room u and v, and imposters need exactly w

seconds to pass through it.

The next line contains two integers e
and tmax (1≤e≤105, 1≤tmax≤108

), denoting the number of predictions and the time for the crewmates to complete all the tasks.

Each of the next e
lines contains three integers p,x,t (1≤p≤k, 1≤x≤n, 1≤t≤tmax), denoting the crewmate p will appear in room x at t

seconds after the game begins.

The last line of each test case contains two integers x
and y (1≤x,y≤n), denoting that the two imposters will spawn in room x and y

when the game begins.

It's guaranteed that ∑n≤104
, ∑m≤2×104 and ∑e≤105 over all test cases.
'''

class Node:
    def __init__(self):
        self.weight = 
        self.