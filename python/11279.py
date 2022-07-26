import heapq
nums = []
heap = []
ans = []
n = int(input())

for _ in range(n):
    nums.append(int(input()))
    
for num in nums:
    if num == 0:
        if len(heap) != 0:
            ans.append(heapq.heappop(heap)[1])
        else:
            ans.append(0)
    else:
        heapq.heappush(heap, (-num, num))
        
for i in ans:
    print(i)
