x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

cond_x = (x2 >= x >= x1) and (y == y1 or y == y2)
cond_y = (y2 >= y >= y1) and (x == x1 or x == x2)

if cond_x or cond_y:
    print("Border")
else:
    print("Inside / Outside")