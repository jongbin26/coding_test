n = int(input())
nums = [int(input()) for _ in range(n)]
k = max(nums)
prime = [False, False] + [True] * (k-1)
m = int(k**0.5)

for i in range(2, m+1):
    if prime[i] == True:
        for j in range(i+i, k, i):
            prime[j] = False
            
for num in nums:
    cnt = 0
    for i in range((num//2)+1):
        if prime[i] and prime[num-i]:
            cnt+=1
    print(cnt)