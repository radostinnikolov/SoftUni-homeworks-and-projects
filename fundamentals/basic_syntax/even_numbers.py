number_of_inputs = int(input())
for i in range(number_of_inputs):
    current = int(input())
    if current % 2 != 0:
        print(f"{current} is odd!")
        break
else:
    print("All numbers are even.")
