e, s, m = map(int, input().split())
a, b, c = 1, 1, 1
n = 1
while(not(a == e and b == s and c ==m)):
    n += 1
    if a + 1 > 15:
        a = 1
    else: a += 1
    if b + 1 > 28:
        b = 1
    else: b += 1
    if c + 1 > 19:
        c = 1
    else: c += 1
print(n)