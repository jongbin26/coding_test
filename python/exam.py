
def partition(number):
    answer = set()
    ## 일단 현재 number도 partition 중 하나 이므로 tuple로 넘겨주고 
    answer.add((number, ))
    ## binary partition: increase x and partition y 
    for x in range(1, number):
        for y in partition(number - x):## new partition of x 
            answer.add(tuple(sorted((x, ) + y)))## like this
    return answer
def findSchedules(workHours, dayHours, pattern):
    space = 0
    temp = []
    for i in pattern:
        if i == '?':
            space += 1
        else:
            workHours -= int(i)
    print(partition(workHours))
findSchedules(3, 2, "??2??00")