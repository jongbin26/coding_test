nums = [0] * 10001
def make(num):
    total = num
    for i in str(num):
        total += int(i)
        
    return total
    
for i in range(1, len(nums)):
    if nums[i] == 0:
        while(True):
            i = make(i)
            if i <= 10000:
                nums[i] = 1
            else:
                break
            
for i in range(1, len(nums)):
    if nums[i] == 0:
        print(i)