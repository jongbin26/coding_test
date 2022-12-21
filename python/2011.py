code = input()
dp = [0] * (len(code) + 1)

dp[0], dp[1] = 1, 1
if code[0] == "0":
    print(0)
    exit()
for i in range(2, len(code)+1):
    if code[i-1] == "0":
        if code[i-2] == "1" or code[i-2] == "2":
            dp[i] = dp[i-2] % 1000000
        else:
            print(0)
            exit()
    else:
        if 10 <= int(code[i-2:i]) <= 26:
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000
        else:
            dp[i] = dp[i-1] % 1000000
print(dp[-1])