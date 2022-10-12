n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

drink = [0] * (n+1)
if n == 1:
    print(wine[1])
    exit()
else:
    drink[1] = wine[1]
    drink[2] = wine[1] + wine[2]
    for i in range(3, n+1):
        drink[i] = max(drink[i-1], drink[i-2]+wine[i], drink[i-3] + wine[i-1] + wine[i])
        
print(max(drink))