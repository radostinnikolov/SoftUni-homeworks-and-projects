tabs_open = int(input())
salary = float(input())
for i in range(tabs_open):
    name_of_tab = input()
    if name_of_tab == "Facebook":
        salary -= 150
    elif name_of_tab == "Instagram":
        salary -= 100
    elif name_of_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))