width = int(input())
length = int(input())
total_pieces = width * length
is_over = False
while is_over is False:
    taken_pieces = input()
    if taken_pieces == "STOP":
        break
    total_pieces -= int(taken_pieces)
    if total_pieces < 0:
        is_over = True
if is_over is False:
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
