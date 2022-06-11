def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

first_num = int(input())
second_num = int(input())
print(f"{factorial(first_num) // factorial(second_num):.2f}")