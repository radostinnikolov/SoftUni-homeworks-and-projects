width = int(input())
length = int(input())
height = int(input())
total_boxes = width * length * height
space_is_over = False
command = input()
while command != "Done":
    total_boxes -= int(command)
    if total_boxes < 0:
        space_is_over = True
        break
    command = input()
if space_is_over is True:
    print(f"No more free space! You need {abs(total_boxes)} Cubic meters more.")
else:
    print(f"{total_boxes} Cubic meters left.")
