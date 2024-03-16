import math
a, b = map(int, input().split())
c, d = map(int, input().split())

son = a * d + b * c
mother = b * d
gcd = math.gcd(son, mother)
print(son//gcd, mother//gcd)