import math
def sum(x):
    if x <= 0:
        return
    expo = int(math.log2(x))
    floor = 2 ** expo
    if x == floor:
        return expo * x // 2 + 1
    diff = x - floor
    return sum(floor) + diff + sum(diff)
a, b = map(int, input().split())
print(sum(b) - sum(a-1))