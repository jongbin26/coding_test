n = int(input())
dp = []
day = [0]*10001
dp = [list(map(int, input().split())) for _ in range(n)]
dp.sort(reverse = True)
ans = 0
for i in dp:
    tmp = i[1]
    while(tmp > 0):
        if day[tmp] == 0:
            day[tmp] = 1
            ans += i[0]
            break
        else:
            tmp -= 1
print(ans)