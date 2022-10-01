n = int(input())
nums = [0] * (n+1)

for i in range(2, n+1):
    nums[i] = nums[i-1] + 1
    if i % 3 == 0:
        nums[i] = min(nums[i], nums[i//3] + 1)
    if i % 2 == 0:
        nums[i] = min(nums[i], nums[i//2] + 1)
        
print(nums[n])