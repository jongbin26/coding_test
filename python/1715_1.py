import heapq
n = int(input())
data = [int(input()) for _ in range(n)]

ans = 0
heapq.heapify(data)
while(len(data) >= 2):
    sum = heapq.heappop(data) + heapq.heappop(data)
    ans += sum
    heapq.heappush(data, sum)
print(ans)

    