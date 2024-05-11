from collections import deque
t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph, indegree = [[] for _ in range(n+1)], [0] * (n+1)
    val = [0] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    target = int(input())
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            val[i] = time[i]
            queue.append(i)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            indegree[i] -= 1
            val[i] = max(val[i], val[x] + time[i])
            if indegree[i] == 0:
                queue.append(i)
    ans.append(val[target])
for i in ans:
    print(i)
