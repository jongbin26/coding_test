def calc(num_list):
    if len(num_list) ==0:
        return 0
    total = 0
    tmp = 1
    even = 0
    for i in num_list:
        if even == 2:
            total += tmp
            tmp = 1
            even = 0
        tmp *= i
        even += 1
    total += tmp
    return total

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
num.sort()

minus = []
plus = []
one = []
for i in num:
    if i <= 0:
        minus.append(i)
    elif i > 1:
        plus.append(i)
    else:
        one.append(i)
plus.sort(reverse=True)
print(calc(plus)+calc(minus)+sum(one))