import sys
sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

for i in graph:
    i.sort()
cnt = 0
ans = [0] * (n+1)
def dfs(x):
    global ans
    global cnt
    cnt += 1
    visited[x] = 1
    ans[x] = cnt
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

dfs(r)
for i in range(1,n+1):
    print(ans[i])