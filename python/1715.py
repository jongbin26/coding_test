import heapq
n = int(input())
nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))

ans = 0

while(len(nums) > 1):
    total = 0
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    
    total = a + b
    ans += total
    heapq.heappush(nums, total)
    
print(ans)
