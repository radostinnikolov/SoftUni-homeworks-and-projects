front = 1
back = 9
for i in range(1, 10):
    for j in range(1, 10):
        if j == front or j == back:
            print("**", end="")
        else:
            print(" ", end="")
    front += 1
    back -= 1
    print("")