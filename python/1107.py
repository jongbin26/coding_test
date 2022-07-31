n = int(input())
ans = abs(100 - n)
m = int(input())
if m:
    err = set(input().split())
else:
    err = set()

for num in range(1000001):
    for char in str(num):
        if char in err:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)