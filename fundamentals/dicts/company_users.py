companies_dict = {}
command = input()
while command != "End":
    input_for_work = command.split(' -> ')
    company = input_for_work[0]
    employee = input_for_work[1]
    if company not in companies_dict:
        companies_dict[company] = [employee]
    else:
        if employee not in companies_dict[company]:
            companies_dict[company].append(employee)
    command = input()
for key in companies_dict:
    print(key)
    for value in companies_dict[key]:
        print(f"-- {value}")