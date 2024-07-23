a, b = map(int, input().split())
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def divisor(n):
    temp = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            temp.append(i) 
            if ( (i**2) != n) : 
                temp.append(n // i)
    temp.sort()
    return temp
ans = []
temp = divisor(b)
for i in range(len(temp)):
    for j in range(i+1, len(temp)):
        if gcd(temp[i], temp[j]) == a:
            ans = [temp[i], temp[j]]
if a == b:
    print(a, a)
else:
    print(ans[0], ans[1])