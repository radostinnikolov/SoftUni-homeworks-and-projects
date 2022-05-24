user_number = int(input())

condition = (user_number >= 100 and user_number <= 200) or user_number == 0

if not condition:
    print("invalid")
