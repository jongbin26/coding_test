import heapq
T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    pile = list(map(int, input().split()))
    q = []
    size = 0
    
    for i in pile:
        heapq.heappush(q, i)
        
    while(len(q) > 1):
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        heapq.heappush(q, a+b)
        size += (a+b)
    ans.append(size)
for i in ans:
    print(i)