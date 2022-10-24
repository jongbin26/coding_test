import heapq

x = int(input())
heap = []
heapq.heappush(heap, 64)

while(True):
    if sum(heap) == x:
        print(len(heap))
        break
    
    small = heapq.heappop(heap)
    small //= 2
    heapq.heappush(heap, small)
    if sum(heap) < x:
        heapq.heappush(heap, small)