n = int(input())
dp = [0] * (n+1)
data = [list(map(int, input().split())) for _ in range(n)]

#뒤에서부터 dp 풀이
for i in range(n-1, -1, -1):
    if i + data[i][0] <= n:
        dp[i] += max(dp[i+1], dp[i+data[i][0]] + data[i][1])
    else: dp[i] = dp[i+1]
print(dp)

# #브루트포스 풀이
# ans = 0
# def retirement(x, sum):
#     global ans
#     if x == n:
#         ans = max(ans, sum)
#         return
#     if x > n:
#         return
#     retirement(x+data[x][0], sum+data[x][1])
#     retirement(x+1, sum)
# retirement(0, 0)
# print(ans)
