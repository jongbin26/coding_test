n = int(input())
gift = [input().split('-') for _ in range(n)]
ans = 0
for i in gift:
    if int(i[1]) <= 90:
        ans += 1
print(ans)