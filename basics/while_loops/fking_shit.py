user_input = input()
condition = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzEnd"
c_counter = 0
o_counter = 0
n_counter = 0
result = ""
final_result = ""
is_over = False
while user_input != "End":
    while user_input in condition:
        if user_input == 'End':
            is_over = True
            break
        if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
            c_counter = 0
            o_counter = 0
            n_counter = 0
            result += " "
            final_result += result
            result = ""
            user_input = input()
            continue
        if user_input == "c":
            if c_counter >= 1:
                result += user_input
                c_counter += 1
                break
            elif c_counter == 0:
                c_counter += 1
                if o_counter >= 1 and n_counter >= 1:
                    continue
                else:
                    break
        if user_input == "o":
            if o_counter >= 1:
                result += user_input
                o_counter += 1
                break
            elif o_counter == 0:
                o_counter += 1
                if c_counter >= 1 and n_counter >= 1:
                    continue
                else:
                    break
        if user_input == "n":
            if n_counter >= 1:
                result += user_input
                n_counter += 1
                break
            elif n_counter == 0:
                n_counter += 1
                if c_counter >= 1 and o_counter >= 1:
                    continue
                else:
                    break
        if c_counter >= 1 or o_counter >= 1 or n_counter >= 1:
            result += user_input
            break
        result += user_input
        user_input = input()
    if is_over is True:
        break
    user_input = input()
print(final_result)


