xorow1 = [['1','2','3'],['4','5','6'],['7','8','9']]

for i in xorow1:
    print(i[0], i[1], i[2])

while True:
    play = str(input("Position: "))
    side = str(input("X or O: "))
    if play == '1':
        xorow1[0][0] = side
    if play == '2':
        xorow1[0][1] = side
    if play == '3':
        xorow1[0][2] = side
    if play == '4':
        xorow1[1][0] = side
    if play == '5':
        xorow1[1][1] = side
    if play == '6':
        xorow1[1][2] = side
    if play == '7':
        xorow1[2][0] = side
    if play == '8':
        xorow1[2][1] = side
    if play == '9':
        xorow1[2][2] = side

    if xorow1[0][0] and xorow1[1][0] and xorow1[2][0] == "x":
        print("X win")
        break
    if xorow1[0][1] and xorow1[1][1] and xorow1[2][1] == "x":
        print("X win")
        break
    if xorow1[0][2] and xorow1[1][2] and xorow1[2][2] == "x":
        print("X win")
        break
    if xorow1[0][1] and xorow1[0][0] and xorow1[0][2] == "x":
        print("X win")
        break
    if xorow1[1][1] and xorow1[1][0] and xorow1[1][2] == "x":
        print("X win")
        break
    if xorow1[2][1] and xorow1[2][0] and xorow1[2][2] == "x":
        print("X win")
        break
    if xorow1[0][0] and xorow1[1][1] and xorow1[2][2] == "x":
        print("X win")
        break
    if xorow1[0][2] and xorow1[1][1] and xorow1[2][0] == "x":
        print("X win")
        break

    #o


    if xorow1[0][0] and xorow1[1][0] and xorow1[2][0] == "o":
        print("X win")
        break
    if xorow1[0][1] and xorow1[1][1] and xorow1[2][1] == "o":
        print("X win")
        break
    if xorow1[0][2] and xorow1[1][2] and xorow1[2][2] == "o":
        print("X win")
        break
    if xorow1[0][1] and xorow1[0][0] and xorow1[0][2] == "o":
        print("X win")
        break
    if xorow1[1][1] and xorow1[1][0] and xorow1[1][2] == "o":
        print("X win")
        break
    if xorow1[2][1] and xorow1[2][0] and xorow1[2][2] == "o":
        print("X win")
        break
    if xorow1[0][0] and xorow1[1][1] and xorow1[2][2] == "o":
        print("X win")
        break
    if xorow1[0][2] and xorow1[1][1] and xorow1[2][0] == "o":
        print("X win")
        break


    for i in xorow1:
        print(i[0], i[1], i[2])

    
    
    

