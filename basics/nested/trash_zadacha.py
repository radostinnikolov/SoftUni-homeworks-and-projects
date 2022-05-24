control = int(input())
first = 0
second = 0
third = 0
fourth = 0
result = ""
password = 0
is_password = False
is_valid = False
successful_counter = 0
while 4 <= control <= 144:
    for i in range(1000, 10000):
        potential_password = str(i)
        counter = 0
        for digit in potential_password:
            if counter == 0:
                first = int(digit)
                counter += 1
                continue
            elif counter == 1:
                second = int(digit)
                counter += 1
                continue
            elif counter == 2:
                third = int(digit)
                counter += 1
                continue
            elif counter == 3:
                fourth = int(digit)
                counter += 1
                break
        if first * second + third * fourth == control and first < second and third > fourth:
            is_valid = True
            result = str(first) + str(second) + str(third) + str(fourth)
            successful_counter += 1
            if successful_counter == 4:
                is_password = True
                password = result
            print(result, end=" ")
            continue
    break
print()
if is_password is True:
    print(f"Password: {password}")
else:
    print("No!")


