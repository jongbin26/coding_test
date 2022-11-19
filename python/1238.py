import heapq
INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while(q):
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost

max_time = 0
for i in range(1, n+1):
    temp = 0
    distance = [INF] * (n+1)
    dijkstra(i)
    temp += distance[x]
    distance = [INF] * (n+1)
    dijkstra(x)
    temp += distance[i]
    max_time = max(max_time, temp)

print(max_time)