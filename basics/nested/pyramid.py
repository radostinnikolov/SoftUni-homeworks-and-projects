number = int(input())
counter = 1
is_over = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        if counter > number:
            is_over = True
            break
        print(counter, end=" ")
        counter += 1
    if is_over:
        break
    print()