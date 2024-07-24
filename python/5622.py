temp = input()
two = ['A', 'B', 'C']
three = ['D', 'E', 'F']
four = ['G', 'H', 'I']
five = ['J', 'K', 'L']
six = ['M', 'N', 'O']
seven = ['P', 'Q', 'R', 'S']
eight = ['T', 'U', 'V']
nine = ['W', 'X', 'Y', 'Z']

ans = 0
for i in temp:
    if i in two:
        ans += 3
    if i in three:
        ans += 4
    if i in four:
        ans += 5
    if i in five:
        ans += 6
    if i in six:
        ans += 7
    if i in seven:
        ans += 8
    if i in eight:
        ans += 9
    if i in nine:
        ans += 10
print(ans)