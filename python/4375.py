while(True):
    try:
        n = int(input())
        temp = '1'
        while True:
            if int(temp) % n == 0:
                break
            temp += '1'
        print(len(temp))
    except:
        break