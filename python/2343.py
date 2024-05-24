n, m = map(int, input().split())
video = list(map(int, input().split()))
left, right = 0, 1000000000
ans = 0
while(left <= right):
    mid = (left + right)//2
    sum, cnt = 0, 1
    flag = False
    for i in video:
        if sum + i <= mid:
            sum += i
        else:
            cnt += 1
            sum = i
            if sum > mid:
                flag = True
                left = mid + 1
                break
    if flag:
        flag = False
        continue
    if cnt > m:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1
print(ans)