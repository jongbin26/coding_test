str1, str2 = input(), input()
dp = [[0] * len(str1) for _ in range(len(str2))]
    
for i in range(len(str1)):
    if str1[i] == str2[0]:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][i-1]
for i in range(len(str2)):
    if str2[i] == str1[0]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i-1][0]

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if str1[j] == str2[i]:
            dp[i][j] = dp[i-1][j-1] + 1
print(dp[len(str2)-1][len(str1)-1])