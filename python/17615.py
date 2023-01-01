n = int(input())
ball = list(input())

def move():
    red_arr = []
    blue_arr = []
    red, blue = 0, 0
    red_switch, blue_switch = False, False
    for i in range(len(ball)-1, -1, -1):
        if ball[i] == 'B':
            red_switch = True
        elif ball[i] == 'R':
            blue_switch = True
        if red_switch and ball[i] == 'R':
            red += 1     
        elif blue_switch and ball[i] == 'B':
            blue += 1
    red_arr.append(red)
    blue_arr.append(blue)
    red, blue = 0, 0
    red_switch, blue_switch = False, False
    for i in range(n):
        if ball[i] == 'B':
            red_switch = True
        elif ball[i] == 'R':
            blue_switch = True
        if red_switch and ball[i] == 'R':
            red += 1     
        elif blue_switch and ball[i] == 'B':
            blue += 1
    red_arr.append(red)
    blue_arr.append(blue)
    return min(min(red_arr), min(blue_arr))
print(move())