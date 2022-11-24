n = int(input())
arr = list(map(int, input().split()))

stack = [arr[n-1]]
ans = [-1]
for i in range(n-2, -1, -1):
    if arr[i] < stack[-1]:
        ans.append(stack[-1])
        stack.append(arr[i])
    else:
        zero = False
        while(arr[i]>=stack[-1]):
            stack.pop()
            if len(stack) == 0:
                stack.append(arr[i])
                ans.append(-1)
                zero = True
                break
        if zero:
            continue
        else:
            ans.append(stack[-1])
            stack.append(arr[i])

for i in range(n-1, -1, -1):
    print(ans[i], end=' ')