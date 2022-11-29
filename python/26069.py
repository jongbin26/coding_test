n = int(input())
people = [list(map(str, input().split())) for _ in range(n)]
dance = []
start = False
for i in people:
    if not start:
        if i[0] == "ChongChong" or i[1] == "ChongChong":
            dance.append(i[0])
            dance.append(i[1])
            start = True
    else:
        if i[0] in dance and i[1] not in dance:
            dance.append(i[1])
        elif i[1] in dance and i[0] not in dance:
            dance.append(i[0])
print(len(dance))
    