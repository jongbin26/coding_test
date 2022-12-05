import heapq
n = int(input())
order = [int(input()) for _ in range(n)]

q=[]
for i in order:
    if i > 0:
        heapq.heappush(q, i)
    else:
        if q:
            tmp = heapq.heappop(q)
            print(tmp)
        else:
            print(0)