import heapq
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
heap = []
for i in range(n):
    for j in range(n):
        if len(heap) < n:
            heapq.heappush(heap, graph[i][j])
        else:
            if heap[0] > graph[i][j]:
                continue
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, graph[i][j])
print(heap[0])