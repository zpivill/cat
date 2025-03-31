
li = []


for i in range(99999):
    num = int(input("nun: "))
    if num == -1:
        break

    li.insert(i, num)
    
    
        
            
            
        
li.sort()
print(li)
li.sort(reverse = True)
print(li)
