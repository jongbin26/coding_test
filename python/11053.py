n = int(input())
nums = list(map(int, input().split()))
val = [0] * n

for i in range(0, len(nums)):
    max_num = 0
    for j in range(0, i):
        if nums[i] > nums[j]:
            max_num = max(max_num, val[j])
    val[i] = max_num + 1
print(max(val))