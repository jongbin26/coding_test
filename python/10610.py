n = input()
arr = []
check = 0
for num in n:
    check += int(num)
    arr.append(int(num))
arr.sort(reverse=True)
if check % 3 == 0 and arr[-1] == 0:
    print(''.join(str(x) for x in arr))
else:
    print(-1)