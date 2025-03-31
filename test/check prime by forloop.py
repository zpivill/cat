num  = int(input("number "))

for i in range(2, num):
    check1 = True
    
    if num% i == 0:
        check1 = False
        break

if check1 == True:
    print(num)