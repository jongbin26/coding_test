n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

best = abs(sum(liquid[-3:]))
triple= []
for i in range(n-2):
    for j in range(i+1, n-1):
        sum = liquid[i] + liquid[j] 
        left = j + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if abs(liquid[mid] + sum) <= best:
                best = abs(liquid[mid] + sum)
                triple = [liquid[i], liquid[j], liquid[mid]]
            if (liquid[mid] + sum) >= 0:
                right = mid - 1
            else:
                left = mid + 1
print(*triple)