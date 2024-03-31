import heapq
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()
heap = []

ans = 0
for i in data:
    if not heap:
        heapq.heappush(heap, i[1])
    else:
        temp = heapq.heappop(heap)
        if i[0] < temp:
            heapq.heappush(heap, temp)
            heapq.heappush(heap, i[1])
        else:
            heapq.heappush(heap, i[1])
    ans = max(ans, len(heap))
print(ans)