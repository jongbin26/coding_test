import heapq
ans = []
t = int(input())
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue, (dist+i[1], i[0]))

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    dijkstra(c)
    
    cnt, max_ans = 0, 0
    for i in distance:
        if not i == 1e9:
            cnt += 1
            if i > max_ans:
                max_ans = i
    ans.append([cnt, max_ans])
for i in ans:
    print(i[0], i[1])
