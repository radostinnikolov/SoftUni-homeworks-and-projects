points_dict = {}
langs_dict = {}
results_input = input()
while results_input != 'exam finished':
    result_for_work = results_input.split('-')
    username = result_for_work[0]
    if result_for_work[1] == 'banned':
        points_dict.pop(username)
    else:
        language = result_for_work[1]
        points = result_for_work[2]
        if username not i n points_dict:
            points_dict[username] = points
        else:
            if points > points_dict[username]:
                points_dict[username] = points
        if language not in langs_dict:
            langs_dict[language] = 0
        langs_dict[language] += 1
    results_input = input()

print("Results:")
for key, value in points_dict.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in langs_dict.items():
    print(f"{key} - {value}")