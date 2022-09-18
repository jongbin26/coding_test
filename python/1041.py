N = int(input())
num = list(map(int, input().split()))
sum_list = []
def calc(n):
    first = (n - 2) * (n - 2) + 4 * (n - 2) * (n -1)
    second = 4 * (n - 2) + 4 * (n - 1)
    third = 4
    return [first, second, third]

if N == 1:
    num.sort()
    print(sum(num)-num[5])
    exit()
space = calc(N)

sum_list.append(min(num[0], num[5]))
sum_list.append(min(num[1], num[4]))
sum_list.append(min(num[2], num[3]))
sum_list.sort()

one_num = sum_list[0]
two_num = sum_list[0] + sum_list[1]
three_num = sum_list[0] + sum_list[1] + sum_list[2]

a = one_num * space[0]
b = two_num * space[1]
c = three_num * space[2]

print(a+b+c)