letters = {"a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
user_input = input()
total_counter = 0
c_counter = 0
o_counter = 0
n_counter = 0
result = ""
while user_input in letters:
    if total_counter == 0:
        result += user_input
        total_counter = 1
        if user_input == "c":
            if c_counter == 1:
                result += user_input
            else:
                c_counter = 1
                if user_input == "o":
                    if o_counter == 1:
                        result += user_input
                    else:
                        o_counter = 1
                        if user_input == "n":
                            if n_counter == 1:
                                result += user_input
                            else:
                                n_counter = 1
                                result += user_input
    user_input = input()
print(result)


