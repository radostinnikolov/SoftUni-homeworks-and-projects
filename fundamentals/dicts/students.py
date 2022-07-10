students = {}
while True:
    command = input()
    if ':' not in command:
        break
    student_input = command.split(':')
    name = student_input[0]
    student_id = student_input[1]
    course = student_input[2]
    student_for_input = name + ' - ' + student_id
    students[student_for_input] = course
i = command.split('_')
searched_course = ' '.join(i)

for key, value in students.items():
    if searched_course in value:
        print(key)