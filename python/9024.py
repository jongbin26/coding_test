t=int(input())
ans = []
for i in range(t):
    n, k= map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()

    temp=int(1e9)
    for j in range(n):
        start, end= j+1, n-1
        while(start<=end):
            mid=(start + end) // 2
            sum = num[j] + num[mid]
            if sum > k:
                end = mid - 1
            else:
                start = mid + 1

            if abs(k - sum) < temp:
                cnt = 1
                temp = abs(k - sum)
            elif abs(k - sum) == temp:
                cnt += 1
    ans.append(cnt)
for i in ans:
    print(i)