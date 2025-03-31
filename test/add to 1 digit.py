a = '69/23/1998'
c =0
sum = 0
Rsum = 0
for i in a:
    if i =="/":
        c=1
    else:
        i = int(i)
        sum +=i

while sum > 9:
    sum = str(sum)
    d1 = int(sum[0])
    d2 = int(sum[1])
    sum = int(d1) + int(d2)
    sum = int(sum)

print(sum)



