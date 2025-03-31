num  = int(input("number "))
for a in range(3, num+1):
    check1 = True
    for i in range(2, a):
        if a% i == 0:
            check1 = False
            break
    if check1 == True:
        print(a)


