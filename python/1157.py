string = input()
alphabet = [0] * 26
for char in string.lower():
    alphabet[ord(char)-97] += 1
max_val = max(alphabet)
ans_arr = []
for i in range(len(alphabet)):
   if alphabet[i] == max_val:
       ans_arr.append(i)
if len(ans_arr) == 1:
    print(chr(ans_arr[0]+97).upper())
else:
    print("?")