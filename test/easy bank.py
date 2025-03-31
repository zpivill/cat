username = 'TALAY'
password = "1234"
key = 0
money = 9000
exit = 0
while exit == 0:
    checkname  = input("Username: ")
    checkpass = input("password")
    if checkname != username or checkpass != password:
        print("Wrong use name try again")
    if checkname == username and checkpass == password:
        key = 1
    while key ==1:
        print(f'account money = {money}')
        print('Input 1 to deposit or 2 to withdraw or 0 to exit')
        userinput = int(input(''))
        if userinput == 1:
            deposit = int(input("Deespoit Money: "))
            money += deposit
            
        if userinput ==2:
            withdraw = int(input("Withdraw Money: "))
            money -= withdraw
        if userinput ==0:
            exit +=1
            key +=1

