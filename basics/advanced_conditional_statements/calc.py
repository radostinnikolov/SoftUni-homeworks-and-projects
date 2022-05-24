number1 = int(input())
number2 = int(input())
operator = input()
result = 0
even_or_odd = "odd"

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
if result % 2 == 0:
    even_or_odd = "even"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{number1} {operator} {number2} = {result} - {even_or_odd}")
if number2 != 0:
    if operator == "/":
        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
    elif operator == "%":
        result = number1 % number2
        print(f"{number1} % {number2} = {result}")
else:
    print(f"Cannot divide {number1} by zero")