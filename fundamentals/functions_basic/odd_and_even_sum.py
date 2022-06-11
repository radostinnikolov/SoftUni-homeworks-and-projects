def odd_and_even_sum(some_number: str):
    even_sum = 0
    odd_sum = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_and_even_sum(number))


