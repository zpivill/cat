limit = int(input("Enter a number: "))
number = 2
while number <= limit:
    prime = True
    div = 2
    while div < number:
        if number%div == 0:
            prime = False
            break
        div += 1
    if prime == True:
        print(number)
    number += 1

