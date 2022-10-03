n = int(input())
ans = []
for _ in range(n):
    num = int(input())
    dp = [0] * (num + 1)
    if num == 1:
        ans.append(1)
        continue
    elif num == 2:
        ans.append(2)
        continue
    elif num == 3:
        ans.append(4)
        continue
    else:
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, num+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        ans.append(dp[num])
        
for i in ans:
    print(i)