students = []
scores = []
max_students = 10
while len(students) < max_students:
    name = input("Name")
    
    while True:
        score_str = input(f"Enter score for {name} (0-100): ")
        score = int(score_str) 
        if 0 <= score <= 100:
            break
        else:
            print("re enter the score")

    students.append(name)
    scores.append(score)


if not students:
    print("No student data entered.")
else:
    total_score = sum(scores)
    average_score = total_score / len(scores)

    max_score = max(scores)
    max_index = scores.index(max_score)
    max_name = students[max_index]

    min_score = min(scores)
    min_index = scores.index(min_score)
    min_name = students[min_index]

    print(f"\nAverage Score: {average_score:.2f}")
    print(f"Highest Score: {max_score} - {max_name}")
    print(f"Lowest Score: {min_score} - {min_name}")

    print("\nStudents Below 50:")
    for i in range(len(students)):
        if scores[i] < 50:
            print(f"{students[i]}: {scores[i]}")