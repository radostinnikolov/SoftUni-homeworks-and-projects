number_of_judges = int(input())
command = input()
sum_overall_marks = 0
number_of_marks = 0
while command != "Finish":
    name_of_presentation = command
    total_mark_for_current = 0
    avg_mark_for_current = 0
    for mark in range(number_of_judges):
        current_mark = float(input())
        total_mark_for_current += current_mark
        avg_mark_for_current = total_mark_for_current / number_of_judges
        sum_overall_marks += current_mark
        number_of_marks += 1
    print(f"{name_of_presentation} - {avg_mark_for_current:.2f}.")
    command = input()
total_avg = sum_overall_marks / number_of_marks
print(f"Student's final assessment is {total_avg:.2f}.")

