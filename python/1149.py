n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

ans = [[0 for _ in range(3)] for _ in range(n)]
ans[0][0] = cost[0][0]
ans[0][1] = cost[0][1]
ans[0][2] = cost[0][2]

for i in range(n):
    ans[i][0] = min(ans[i-1][1], ans[i-1][2]) + cost[i][0]
    ans[i][1] = min(ans[i-1][0], ans[i-1][2]) + cost[i][1]
    ans[i][2] = min(ans[i-1][0], ans[i-1][1]) + cost[i][2]
print(min(ans[n-1]))