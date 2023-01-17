n = int(input())
arr = list(map(int, input().split()))
left, right = 0, len(arr)-1

ans = int(2e9)
while(left < right):
    if ans > abs(arr[left] + arr[right]):
        ans = abs(arr[left] + arr[right])
        ans_arr = [arr[left], arr[right]]
    #left move
    if abs(arr[left+1] + arr[right]) < abs(arr[left] + arr[right-1]):
        left += 1
    else:
        right -= 1
        
print(ans_arr[0], ans_arr[1])