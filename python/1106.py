c, n = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]
infos.sort(key = lambda x:x[1])
dp = [int(1e9)] * (c+infos[-1][1])
for info in infos:
    dp[info[1]] = min(dp[info[1]], info[0])
for info in infos:
    for i in range(info[1], c+infos[-1][1]):
        if i-info[1] > 0:
            dp[i] = min(dp[i], dp[i-info[1]] + info[0])
print(min(dp[c:]))