n = int(input())

student = {}

for _ in range(n):
    entry = input().split()
    if entry[0] not in student:
        student[entry[0]] = [float(entry[1])]
    else:
        student[entry[0]].append(float(entry[1]))

for student, grades in student.items():
    average = sum(grades) / len(grades)
    print(f'{student} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {average:.2f})')