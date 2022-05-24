number_of_msg = int(input())
for i in range(number_of_msg):
    command = int(input())
    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command < 88:
        print("GREAT!")
    else:
        print("Bye.")