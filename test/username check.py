
check1 = False
check2 = False
check3 = False
check4 = False
count = 0


while count <3:
    user = input(' ')
    asp = user.split('_')
    print(asp)
    
    if len(asp) == 2:
        check1 =True
    if asp[0].isalpha() == True:
        check2 = True
    if asp[1].isdigit() ==True:
        check3 = True
    if asp[0].islower() == True:
        check4 = True
    print(check1)
    print(check2)
    print(check3)
    print(check4)
    if check1 ==True and check2 ==True and check3 == True and check4 == True:
        print(user)
        break
    count += 1
    if count ==3:
        break
