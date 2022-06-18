def add_lesson(lesson):
    if lesson not in course_list:
        course_list.append(lesson)
    return


def insert_lesson(lesson, lesson_index):
    if lesson not in course_list:
        course_list.insert(lesson_index, lesson)
    return


def remove_lesson(course_list, lesson):
    if lesson in course_list:
        course_list.remove(lesson)
        if f"{lesson}-Exercise" in course_list:
            course_list.remove(f"{lesson}-Exercise")
    return



def swap_lesson(course_list, lesson1, lesson2):
    if lesson1 in course_list and lesson2 in course_list:
        index_1 = course_list.index(lesson1)
        index_2 = course_list.index(lesson2)
        course_list[index_1], course_list[index_2] = course_list[index_2], course_list[index_1]
        check_exercise(lesson1)
        check_exercise(lesson2)
    return

def add_exercise(lesson):
    if lesson in course_list and f"{lesson}-Exercise" not in course_list:
        index_of_exercise = course_list.index(lesson) + 1
        course_list.insert(index_of_exercise, f"{lesson}-Exercise")
    elif lesson not in course_list:
        add_lesson(lesson)
        index_of_exercise = course_list.index(lesson) + 1
        course_list.insert(index_of_exercise, f"{lesson}-Exercise")
    return

def check_exercise(lesson):
    if f"{lesson}-Exercise" in course_list:
        index_exer = course_list.index(f"{lesson}-Exercise")
        index_less = course_list.index(lesson)
        item = course_list.pop(index_exer)
        course_list.insert(index_less + 1, item)
    return


course_list = [course for course in input().split(", ")]
command = input()
while command != "course start":
    command_list = command.split(":")
    lesson_name = command_list[1]
    order = command_list[0]
    if order == "Add":
        add_lesson(lesson_name)
    elif order == "Insert":
        lesson_index = int(command_list[2])
        insert_lesson(lesson_name, lesson_index)
    elif order == "Remove":
        remove_lesson(course_list, lesson_name)
    elif order == "Swap":
        lesson_name2 = command_list[2]
        swap_lesson(course_list, lesson_name, lesson_name2)
    elif order == "Exercise":
        add_exercise(lesson_name)
    command = input()
for i in range(len(course_list)):
    print(f"{i+1}.{course_list[i]}", end='\n')
