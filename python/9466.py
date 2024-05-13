import sys
sys.setrecursionlimit(10**5)
t = int(input())
ans = []

def dfs(x):
    global temp
    visited[x] = True
    cycle.append(x)
    next = graph[x]
    if visited[next]:
        if next in cycle:
            temp += cycle[cycle.index(next):]
        return
    else:
        dfs(next)

for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [1] + [0] * (n)
    temp = []
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    ans.append(n - len(temp))

for i in ans:
    print(i)