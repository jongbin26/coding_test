n = int(input())
nums = list(map(int, input().split()))
val = [1] * (n)

for i in range(1, n):
    for j in range(0, i):
        if nums[j] > nums[i]:
            val[i] = max(val[i], val[j] + 1)
    
print(n-max(val))
    