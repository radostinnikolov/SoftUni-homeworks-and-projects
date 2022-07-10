elements_dict = {}
elements = input().lower().split()
for el in elements:
    if el not in elements_dict:
        elements_dict[el] = 0
    elements_dict[el] += 1
list_for_print = []
for key, value in elements_dict.items():
    if value % 2 != 0:
        list_for_print.append(key)
print(' '.join(list_for_print))

