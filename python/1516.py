from collections import deque
n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
arr = [0]
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(1, len(temp)-1):
        graph[temp[j]].append(i+1)
        indegree[i+1]+=1
queue = deque()
ans = [0] * (n+1)
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
        ans[i] = arr[i][0]
while queue:
    x = queue.popleft()
    for i in graph[x]:
        ans[i] = max(ans[i], ans[x] + arr[i][0])
        indegree[i] -= 1
        if not indegree[i]:
            queue.append(i)
for i in ans[1:]:
    print(i)