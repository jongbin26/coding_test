from collections import deque
n, m = map(int, input().split())
sequnence = []
for _ in range(m):
    sequnence.append(list(map(int, input().split()))[1:])
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for arr in sequnence:
    for i in range(len(arr)-1):
        graph[arr[i]].append(arr[i+1])
        indegree[arr[i+1]] += 1
ans = []
queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    x = queue.popleft()
    ans.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
if len(ans) != n:
    print(0)
else:
    for i in ans:
        print(i)