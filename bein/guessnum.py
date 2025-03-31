import random

randomNum = random.randint(0,1000)
guess = int(input("guess a number"))
print(randomNum)

if randomNum == guess:
    print("correct guess")
else:
    print(f"the correct number was, {randomNum}")

