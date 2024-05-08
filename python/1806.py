n, s = map(int ,input().split())
arr = list(map(int, input().split()))

if len(arr) >= 2:
    left, right = 0, 1
sum = arr[left] + arr[right]
while(True):
    if arr[left] + arr[right] + arr[right+1] < s:
        right += 1
        sum = arr[left] + arr[right] + arr[right+1]
    else:
        arr -= sum[left]
        left += 1
    