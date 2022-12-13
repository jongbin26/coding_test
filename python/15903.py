import heapq
n, m = map(int, input().split())
num = list(map(int, input().split()))
q = []
for i in num:
    heapq.heappush(q, i)

for _ in range(m):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a+b)
    heapq.heappush(q, a+b)

print(sum(q))