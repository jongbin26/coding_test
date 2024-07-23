n = int(input())
table= [False,False] + [True]*(9999)
primes=[]
for i in range(2,10001):
  if table[i]:
    primes.append(i)
    for j in range(2*i, 10001, i):
        table[j] = False

ans = []
for _ in range(n):
    num = int(input())
    temp = []
    for prime in primes:
       if prime > num:
          break
       else:
          if num - prime in primes:
             temp.append([prime, num-prime])
    ans.append(temp[len(temp)//2])
for i in ans:
   print(i[1], i[0])