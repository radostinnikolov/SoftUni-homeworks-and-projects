not_good_marks = int(input())
counter = 0
succ_counter = 0
last_problem = ""
total_marks = 0
while counter < not_good_marks:
    problem_name = input()
    if problem_name == "Enough":
        break
    mark = int(input())
    if mark <= 4:
        counter += 1
    last_problem = problem_name
    total_marks += mark
    succ_counter += 1
avg_points = total_marks / succ_counter
if problem_name == "Enough":
    print(f"Average score: {avg_points:.2f}")
    print(f"Number of problems: {succ_counter}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {not_good_marks} poor grades.")