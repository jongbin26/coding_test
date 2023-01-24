n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, len(arr)-1
ans_val = int(2e9)
while(left<right):
    temp = arr[left] + arr[right]
    if abs(temp) < ans_val:
        ans_val = abs(temp)
        ans = [arr[left], arr[right]]
    if abs(arr[left+1] + arr[right]) < abs(arr[left] + arr[right-1]):
        left += 1
    else:
        right -= 1
print(ans[0], ans[1])