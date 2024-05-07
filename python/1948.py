from collections import deque
n = int(input())
m = int(input())

time = [0] * (n+1)
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
cnt = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    indegree[b] += 1

start, end = map(int, input().split())

queue = deque([])
queue.append(start)

while queue:
    now = queue.popleft()
    for i in graph[now]:
        indegree[i[1]] -= 1
        if time[i[1]] < time[now] + i[0]:
            time[i[1]] = time[now] + i[0]
            cnt[i[1]] = [now]
        elif time[i[1]] == time[now] + i[0]:
            cnt[i[1]].append(now)

        if indegree[i[1]] == 0:
            queue.append(i[1])
queue = deque([end])
route = set()
while queue:
    now = queue.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            queue.append(x)

print(time[end])
print(len(route))