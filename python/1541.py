string = input()
nums = []
num = ''

for i in string:
    if i == '-':
        nums.append(num)
        num = ''
        nums.append('-')
    elif i == '+':
        nums.append(num)
        num = ''
        nums.append('+')
    else:
        num += i
nums.append(num)

while('+' in nums):
    sum = 0
    idx = nums.index('+')
    sum = int(nums[idx-1])+int(nums[idx+1])
    del nums[idx-1]
    del nums[idx-1]
    del nums[idx-1]
    nums.insert(idx-1, sum)

res = int(nums[0])
for i in range(1, len(nums)):
    if nums[i] != '-':
        res -= int(nums[i])
print(res)