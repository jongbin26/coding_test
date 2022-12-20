game = []
while(True):
    line = input()
    if line == "end":
        break
    game.append(line)
ans = []

def tictactoe(line):
    o_finish, x_finish = isFinish(line)
    x_count = 0
    o_count = 0
    no_count = 0
    for i in line:
        if i == "X":
            x_count += 1
        elif i == "O":
            o_count += 1
        else:
            no_count += 1
            
    if x_count == o_count:
        #같은 횟수
        if x_finish == o_finish == 0:
            #완성된 줄이 없는 상황
            return 0
        else:
            #완성된 줄이 있는 상황
            if o_finish > x_finish and x_finish == 0:
                return 1
            else:
                return 0
    elif x_count == o_count + 1:
        #x가 하나 많은 상황
        if x_finish == o_finish == 0:
            #완성된 줄이 없는 상황
            if no_count == 0:
                #게임판이 가득찼으나 완성된 줄은 없는 상황
                return 1
            else:
                return 0
        else:
            #완성된 줄이 있는 상황
            if x_finish > o_finish and o_finish == 0:
                return 1
            else:
                return 0
    else:
        return 0

def isFinish(line):
    o_finish = 0
    x_finish = 0
    if line[0] == line[1] == line[2]:
        if line[0] == "O":
            o_finish += 1
        elif line[0]=="X":
            x_finish += 1
    if line[3] == line[4] == line[5]:
        if line[3] == "O":
            o_finish += 1
        elif line[3]=="X":
            x_finish += 1
    if line[6] == line[7] == line[8]:
        if line[6] == "O":
            o_finish += 1
        elif line[6]=="X":
            x_finish += 1
    if line[0] == line[3] == line[6]:
        if line[0] == "O":
            o_finish += 1
        elif line[0]=="X":
            x_finish += 1
    if line[1] == line[4] == line[7]:
        if line[1] == "O":
            o_finish += 1
        elif line[1]=="X":
            x_finish += 1
    if line[2] == line[5] == line[8]:
        if line[2] == "O":
            o_finish += 1
        elif line[2]=="X":
            x_finish += 1
    if line[0] == line[4] == line[8]:
        if line[0] == "O":
            o_finish += 1
        elif line[0]=="X":
            x_finish += 1
    if line[2] == line[4] == line[6]:
        if line[2] == "O":
            o_finish += 1
        elif line[2]=="X":
            x_finish += 1
    return o_finish, x_finish

for line in game:
    if tictactoe(line):
        print("valid")
    else:
        print("invalid")
    