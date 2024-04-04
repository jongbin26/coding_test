import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)
ans = [0] * (n+1)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
            ans[i] = x
dfs(1)
for i in range(2, len(ans)):
    print(ans[i])