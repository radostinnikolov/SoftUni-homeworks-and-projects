user_fruit = input()
user_day = input()
amount = float(input())

fruits = {"banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"}
workday = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
weekend = {"Saturday", "Sunday"}

condition1 = user_fruit not in fruits
condition2 = user_day not in workday
condition3 = user_day not in weekend

result = 0
if condition1 or (condition2 and condition3):
    print("error")
elif user_day in workday:
    if user_fruit == "banana":
        result = amount * 2.5
    elif user_fruit == "apple":
        result = amount * 1.2
    elif user_fruit == "orange":
        result = amount * 0.85
    elif user_fruit == "grapefruit":
        result = amount * 1.45
    elif user_fruit == "kiwi":
        result = amount * 2.7
    elif user_fruit == "pineapple":
        result = amount * 5.5
    elif user_fruit == "grapes":
        result = amount * 3.85
    print(f"{result:.2f}")
elif user_day in weekend:
    if user_fruit == "banana":
        result = amount * 2.7
    elif user_fruit == "apple":
        result = amount * 1.25
    elif user_fruit == "orange":
        result = amount * 0.9
    elif user_fruit == "grapefruit":
        result = amount * 1.6
    elif user_fruit == "kiwi":
        result = amount * 3
    elif user_fruit == "pineapple":
        result = amount * 5.6
    elif user_fruit == "grapes":
        result = amount * 4.2
    print(f"{result:.2f}")




