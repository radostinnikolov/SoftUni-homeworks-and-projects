number_of_electrons = int(input())
electrons_left = True
shell_number = 1
output = []
while electrons_left:
    if number_of_electrons == 0:
        break
    shell_volume = 2 * shell_number ** 2
    if number_of_electrons >= shell_volume:
        output.append(shell_volume)
        number_of_electrons -= shell_volume
    elif number_of_electrons < shell_volume:
        output.append(number_of_electrons)
        break
    shell_number += 1
print(output)