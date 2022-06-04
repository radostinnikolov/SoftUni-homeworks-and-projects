user_input = input().split()
user_input_as_int = [int(i) for i in user_input]
final_list = []
for num in user_input_as_int:
    final_list.append(-num)
print(final_list)
