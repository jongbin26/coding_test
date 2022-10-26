n = int(input())
num = [0] * 20000001
card = list(map(int , input().split()))
for i in card:
    num[i + 10000000] = 1
m = int(input())
test = list(map(int , input().split()))
ans = []
for i in test:
    if num[i + 10000000] == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')