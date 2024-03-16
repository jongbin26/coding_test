import math
n = int(input())

def checkPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
       if(x%i == 0):
           return False
    return True

ans = []
temp = ['1', '3', '7', '9']
initial = ['2', '3', '5', '7']

def dfs(str, h):
    if h == n-1:
        ans.append(str)
        return
    for i in range(4):
        new_str  = str + temp[i]
        if checkPrime(int(new_str)):
            dfs(new_str, h+1)
for i in range(4):
    dfs(initial[i], 0)
for i in ans:
    print(int(i))
