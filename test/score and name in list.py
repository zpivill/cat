
li = []
Tname = ""
Score = 0

for i in range(99999):
    Tname = input("Name: ")
    if Tname == "STOP":
        break
    Score = int(input("Score: "))
    li.insert(i,[Tname, Score])

print("Student List:")
for i in li:
    print(i[0], i[1])


    