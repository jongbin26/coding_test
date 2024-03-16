n = int(input())
m = int(input())
s = input()

k= [0] * m
for i in range(0, m-1):
    if s[i:i+3] == 'IOI':
        k[i] = 1

for i in range(0, m-1):
    if k[i] > 0 and k[i+2] > 0:
        k[i+2] = k[i] + 1

ans = 0
for i in range(m):
    if k[i] >= n:
        ans += 1
print(ans)