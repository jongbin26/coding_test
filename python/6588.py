import math

def primeNumber(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i ==0:
            return False
    return True

a = 1
ans = []
while(a != 0):
    a = int(input())
    for i in range(2, a):
        if primeNumber(i) == True:
            if primeNumber(a-i) == True:
                ans.append(str(a)+" = "+str(i)+" + "+str(a-i))
                break
                
for res in ans:
    print(res)