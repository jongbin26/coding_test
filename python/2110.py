n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

left, right = 1, arr[-1] - arr[0]
while left <= right:
    mid = (left + right) // 2
    cnt, now = c, arr[0]
    for i in range(1, n):
        if arr[i] >= now + mid:
            cnt -= 1
            now = arr[i]
    if cnt <= 1:
        left = mid + 1
        ans = mid
    else: right = mid - 1
print(ans)
