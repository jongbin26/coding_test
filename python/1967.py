import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[] for _ in range(n+1)]
weight = [0] * (n+1)

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    weight[b] = c

ans = 0
def dfs(x):
    global ans
    if not graph[x]:
        return weight[x]
    sum = []
    max_val = 0
    for i in graph[x]:
            temp = dfs(i)
            max_val = max(max_val, temp)
            sum.append(temp)
    sum.sort()
    if len(sum) == 1:
         ans = max(ans, sum[-1])
    else:
         ans = max(ans, sum[-1] + sum[-2])
    return max_val + weight[x]
dfs(1)
print(ans)