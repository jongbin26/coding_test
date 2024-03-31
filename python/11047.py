n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
ans = 0
for coin in coins:
    if k == 0:
        print(ans)
        exit(0)
    if k >= coin:
        temp = k // coin
        k = k % coin
        ans += temp
    else:
        continue
print(ans)