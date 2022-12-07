import heapq
n = int(input())
num = [int(input()) for _ in range(n)]
max_heap = []
min_heap = []
for i in range(n):
    if i % 2 == 0:
        heapq.heappush(max_heap, (-num[i] ,num[i]))
    else:
        heapq.heappush(min_heap, num[i])
    
    if max_heap and min_heap:
        if max_heap[0][1] > min_heap[0]:
            temp1 = heapq.heappop(max_heap)
            temp2 = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-temp2, temp2))
            heapq.heappush(min_heap, temp1[1])
    print(max_heap[0][1])