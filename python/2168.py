x, y = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
num = gcd(x, y)

small_x = x // num
small_y = y // num

if small_x < small_y:
    small_x, small_y = small_y, small_x

comp = 0
for i in range(1, small_x):
    comp += (small_y*i//small_x) * 2
unit = small_x * small_y - comp

print(unit * num)