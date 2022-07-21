n = int(input())
lines = []
lines2 = []
for _ in range(n):
    lines.append(list(map(str, input().split())))

for line in lines:
    tmp = list()
    for word in line:
        tmp.append(''.join(reversed(word)))
    lines2.append(tmp)
    
for line in lines2:
    for word in line:
        print(word, end=' ')
    print()