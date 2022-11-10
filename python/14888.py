from collections import deque
n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_num = int(-1e9)
min_num = int(1e9)

def dfs(k, stack):
    global min_num, max_num
    if k == 0:
        #계산
        calc = nums[0]
        for i in range(1, len(nums)):
            if stack[i-1] == 0:
                calc += nums[i]
            elif stack[i-1] == 1:
                calc -= nums[i]
            elif stack[i-1] == 2:
                calc *= nums[i]
            elif stack[i-1] == 3:
                if (nums[i] > 0 and calc < 0) or (nums[i] < 0 and calc > 0):
                    calc = -(abs(calc) // abs(nums[i]))
                else:
                    calc = abs(calc) // abs(nums[i])
        min_num = min(min_num, calc)
        max_num = max(max_num, calc)
        return
    
    for i in range(len(oper)):
        if oper[i] > 0:
            oper[i] -= 1
            stack.append(i)
            dfs(k-1, stack)
            oper[i] += 1
            stack.pop()
            
            
stack = []
dfs(n-1, stack)
print(max_num)
print(min_num)