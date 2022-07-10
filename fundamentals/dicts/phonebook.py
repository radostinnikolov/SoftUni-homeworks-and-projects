phonebook = {}
while True:
    user_input = input()
    if '-' not in user_input:
        break
    contact = user_input.split('-')
    name = contact[0]
    phone = contact[1]
    if name not in phonebook:
        phonebook[name] = ''
    phonebook[name] = phone
for i in range(int(user_input)):
    name_for_search = input()
    if name_for_search not in phonebook:
        print(f"Contact {name_for_search} does not exist.")
    else:
        print(f"{name_for_search} -> {phonebook[name_for_search]}")
