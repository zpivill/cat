all = 10
max = -10000000
min = 10000000000
sum = 0
for i in range(all):
    
    num = int(input("number"))
    sum +=num
    if num <= min:
        min = num
    if num >= max:
        max = num
avg = sum/10

print(sum)
print(max)
print(min)
print(avg)