gift_list = input().split(" ")
command = input()

while command != "No Money":
    if "OutOfStock" in command:
        command_list = command.split(" ")
        while command_list[1] in gift_list:
            index = gift_list.index(command_list[1])
            gift_list[index] = "None"
    elif "Required" in command:
        command_list = command.split(" ")
        if int(command_list[2]) <= len(gift_list) - 1:
            index = int(command_list[2])
            gift_list[index] = command_list[1]
    elif "JustInCase" in command:
        command_list = command.split(" ")
        gift_list[-1] = command_list[1]
    command = input()
for item in gift_list:
    if item != "None":
        print(item, end=" ")



