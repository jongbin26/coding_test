import sys
n = int(input())
arr = list(map(int, input().split()))
left, right = 0, len(arr)-1
ans = []
ans_val = float('inf')
while(left < right):
    temp = arr[left] + arr[right]
    if abs(temp) < ans_val:
        ans_val = abs(temp)
        ans = [arr[left], arr[right]]
    if temp > 0:
        right -= 1
    else:
        left += 1
for i in ans:
    print(i, end=' ')