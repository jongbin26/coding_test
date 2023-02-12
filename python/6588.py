import math
prime = [0] * 1000001
def primeNumber(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i ==0:
            return False
    return True
for i in range(2, 1000001):
    if primeNumber(i) == True:
        prime[i] = 1
    else:
        prime[i] = 0
ans = []
while(True):
    a = int(input())
    if a == 0:
        break
    for i in range(3, a):
        if prime[i] and prime[a-i]:
            ans.append(str(a) + " = " + str(i) + " + " + str(a-i))
            break
for i in ans:
    print(i) 