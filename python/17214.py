poly = input()
term1_bool = False
term2_bool = False
if poly == "0":
    print('W')
    exit()
if 'x' in poly:
    for i in range(0, len(poly)):
        if poly[i] == 'x':
            term2 = poly[0:i]
            term2_bool = True
            if i < len(poly)-1:
                term1_bool = True
                if poly[i+1] == "+":
                    term1 = poly[i+2:]
                else:
                    term1 = poly[i+1:]
            break
else:
    term1 = poly
    term1_bool = True

if term1_bool and term2_bool:
    a = str(int(int(term2)/2))
    b = str(term1)
    if a == "1":
        a = ""
    elif a == "-1":
        a = "-"
    if b == "1":
        b = ""
    elif b == "-1":
        b = "-"
    if int(term1) < 0:
        print(a+"xx"+b+"x+"+"W")
    else:
        print(a+"xx+"+b+"x+"+"W")
elif term1_bool and not term2_bool:
    b = str(term1)
    if b == "1":
        b = ""
    elif b == "-1":
        b = "-"
    print(b+"x+"+"W")
elif not term1_bool and term2_bool:
    a = str(int(int(term2)/2))
    if a == "1":
        a = ""
    elif a == "-1":
        a = "-"
    print(a + "xx+W")