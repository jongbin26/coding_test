K, N = map(int, input().split())
nums = []
for _ in range(K):
    nums.append(int(input()))
start, end = 1, max(nums)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in nums:
        lines += i // mid
    
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)