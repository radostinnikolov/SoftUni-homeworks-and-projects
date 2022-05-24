number = int(input())
for current_number in range(1111, 9999 + 1):
    current_number_as_sting = str(current_number)
    is_special = True
    for digit in current_number_as_sting:
        if int(digit) == 0:
            is_special = False
            break
        if number % int(digit) != 0:
            is_special = False
            break
        else:
            continue
    if is_special:
        print(current_number_as_sting, end=" ")


