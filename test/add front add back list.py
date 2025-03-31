Set = [0]
Thelist1 = []
Thelist2 = []
Thelist3 = []

set1 =  int(input(""))

for i in range(set1):
    Liset1= int(input(""))
    Thelist1.append(Liset1)


set2  = (input(""))
Thelist2 = set2.split()
Thelist2 = [int(num) for num in Thelist2]


while True:
    set3 = int(input(""))

    if set3 == -1:
        break

    Thelist3.append(set3)


a =len(Thelist1)
b =len(Thelist2)
c = len(Thelist3)
z = a+b+c

newb = c//2+1
newa = (b+c)//2+1
k =0
check = 0
for i in Thelist3:
        Set.insert(k, i)
        check += 1
        if k == 0:
            check+=1
        if check%2 == 0:
            k+=1
check = 0
for g in Thelist2:
        Set.insert(newb, g)
        check +=1
        if newb == b//2+1:
            check+=1
        if check%2 == 0:
            newb +=1
check =0
for h in Thelist1:
        Set.insert(newa, h)
        check +=1
        if newa == b//2+1:
            check+=1
        if check%2 == 0:
            newa +=1
        
print(Set)