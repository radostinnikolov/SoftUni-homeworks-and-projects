degrees = int(input())
time_of_day = input()
outfit = ""
shoes = ""
con1 = 10 <= degrees <= 18
con2 = 18 < degrees <= 24
con3 = degrees >= 25

if time_of_day == "Morning":
    if con1:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif con2:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif con3:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if con1:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif con2:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif con3:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

