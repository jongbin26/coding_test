n, l = map(int, input().split())
piece = [list(map(int, input().split())) for _ in range(n)]
piece.sort()
ans = 0
temp = piece[0][0]
for i in range(len(piece)):
    if temp < piece[i][0]:
        temp = piece[i][0]
    section = piece[i][1] - temp
    if section % l == 0:
        ans += section // l
        temp += l * (section // l)
    else:
        ans += section // l + 1
        temp += l * (section // l) + l
print(ans)