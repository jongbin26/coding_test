n, m = map(int, input().split())
checkpoint = [int(input()) for _ in range(n)]
checkpoint.sort()
start, end = 0, checkpoint[-1] * m

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in checkpoint:
        temp += mid // i
    
    if temp >= m:
        end = mid - 1
    else:
        start = mid + 1
print(start)