courses_dict = {}
command = input()
while command != "end":
    input_for_work = command.split(' : ')
    course_name = input_for_work[0]
    student_name = input_for_work[1]
    if course_name not in courses_dict:
        courses_dict[course_name] = []
    courses_dict[course_name].append(student_name)
    command = input()
for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for name in value:
        print(f"-- {name}")