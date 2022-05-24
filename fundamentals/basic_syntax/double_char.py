command = input()
while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for char in command:
        print(char + char, end="")
    print("")
    command = input()
