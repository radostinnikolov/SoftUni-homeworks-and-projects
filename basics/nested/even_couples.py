first_number = int(input())
second_number = int(input())
first_diff = int(input())
second_diff = int(input())
result = ""
for first_half in range(first_number, first_number + first_diff + 1):
    is_prime = True
    for cond in range(2, first_half):
        if first_half % cond == 0:
            is_prime = False
            continue
    if is_prime is True:
        result += str(first_half)
        for second_half in range(second_number, second_number + second_diff + 1):
            is_prime2 = True
            for cond2 in range(2, second_half):
                if second_half % cond2 == 0:
                    is_prime2 = False
                    continue
            if is_prime2 is True:
                result += str(second_half)
                print(result)
                result = str(first_half)
                continue
        result = ""
        continue


