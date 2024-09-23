m = int(input())

start = 0
end = m * 5

def find(x):
    cnt = 0
    while(x >= 5):
        x //= 5
        cnt += x
    return cnt

while(start <= end):
    mid = (start + end) // 2
    if(find(mid) > m):
        end = mid-1
        continue
    if(find(mid) < m):
        start = mid+1
        continue
    print(mid - mid % 5)
    exit()
print(-1)