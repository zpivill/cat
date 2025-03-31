numbers = []
unique_numbers = set()

print("Num: ")

while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'done':
        break

    
    num = float(user_input)
    numbers.append(num)
    unique_numbers.add(num)
    

num_unique = len(unique_numbers)

print(f"\nNumber of different numbers: {num_unique}")

if num_unique > 0:
    print("different:", ", ".join(map(str, sorted(unique_numbers))))