def ccw(x1, y1, x2, y2, x3, y3):
    temp = x1 * y2 + x2 * y3 + x3 * y1
    temp = temp - y1 * x2 - y2 * x3 - y3 * x1
    if temp > 0:
        print(1)
    elif temp < 0:
        print(-1)
    else:
        print(0)

point = [list(map(int, input().split())) for _ in range(3)]
ccw(point[0][0], point[0][1], point[1][0], point[1][1], point[2][0], point[2][1])