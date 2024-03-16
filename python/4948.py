import math
nums, ans = [], []
while(True):
    num = int(input())
    if num == 0 : break
    else: nums.append(num)

sosu = [True for _ in range(max(nums)*2+1)]
sosu[1] = False
for i in range(2, int(math.sqrt(max(nums)*2))+1):
    if sosu[i] == True:
        j = 2
        while(i * j <= max(nums)*2):
            sosu[i*j] = False
            j += 1

for num in nums:
    temp = 0
    for i in range(num+1, num * 2 + 1):
        if sosu[i] == True:
            temp += 1
    ans.append(temp)
for i in ans:
    print(i)