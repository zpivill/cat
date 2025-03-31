Paragraph = input('Inout ')
alpha = 0
digit =0
special = 0
for i in Paragraph:
    if i.isalpha() == True:
        alpha +=1
    elif i.isdigit() == True:
        digit +=1
    else:
        special += 1

print(alpha)
print(digit)
print(special)

