month = input()
days_in_hotel = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
elif month == "June" or month == "September":
    price_studio = 75.2
    price_apartment = 68.7
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

total_studio = price_studio * days_in_hotel
total_apartment = price_apartment * days_in_hotel

if month == "May" or month == "October":
    if 7 < days_in_hotel <= 14:
        total_studio *= 0.95
    elif days_in_hotel > 14:
        total_studio *= 0.7
elif month == "June" or month == "September":
    if days_in_hotel > 14:
        total_studio *= 0.8

if days_in_hotel > 14:
    total_apartment *= 0.9

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
