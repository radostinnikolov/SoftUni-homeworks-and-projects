def multiply(a, b):
    return a * b


def divide(a, b):
    return int(a / b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(operation, first_num, second_num):
    result = 0
    if operation == "multiply":
        result = multiply(first_num, second_num)
    elif operation == "divide":
        result = divide(first_num, second_num)
    elif operation == "add":
        result = add(first_num, second_num)
    elif operation == "subtract":
        result = subtract(first_num, second_num)
    return result

input_operator = input()
first_number = int(input())
second_number = int(input())
print(calculate(input_operator,first_number,second_number))