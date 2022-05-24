type_of_movie = input()
rows = int(input())
columns = int(input())
income = 0

capacity = rows * columns
if type_of_movie == "Premiere":
    income = capacity * 12
elif type_of_movie == "Normal":
    income = capacity * 7.5
elif type_of_movie == "Discount":
    income = capacity * 5
print(f"{income:.2f} leva.")