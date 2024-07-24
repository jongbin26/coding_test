def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
new_num = []
for i in range(1, n):
    new_num.append(num[i]-num[i-1])
res = new_num[0]
for i in range(1, n-1):
    res = gcd(res, new_num[i])

ans = set()
for i in range(2, int(res**0.5)+1):
    if res % i == 0:
        ans.add(i)
        ans.add(res // i)
ans.add(res)
print(*sorted(list(ans)))