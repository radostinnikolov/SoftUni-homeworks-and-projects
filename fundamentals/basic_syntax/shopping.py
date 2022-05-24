budget = int(input())
user_input = input()
total = 0
while user_input != "End":
    total += int(user_input)
    if total > budget:
        print("You went in overdraft!")
        break
    user_input = input()
else:
    print("You bought everything needed.")