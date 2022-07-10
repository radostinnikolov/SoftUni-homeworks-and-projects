all_grades = {}
grades_for_print = {}
number_of_pairs = int(input())
for i in range(0, number_of_pairs*2, 2):
    name = input()
    grade = float(input())
    if name not in all_grades:
        all_grades[name] = []
    all_grades[name].append(grade)
for key, value in all_grades.items():
    result = sum(value) / len(value)
    if result >= 4.5:
        grades_for_print[key] = result
for key, value in grades_for_print.items():
    print(f"{key} -> {value:.2f}")
