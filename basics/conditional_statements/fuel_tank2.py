type_of_fuel = input()
fuel_amount = float(input())
card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

gasoline_discount = 0.18
diesel_discount = 0.12
gas_discount = 0.08

if card == "Yes":
    gasoline_price -= gasoline_discount
    diesel_price -= diesel_discount
    gas_price -= gas_discount
elif card == "No":
    pass
total_gasoline = fuel_amount * gasoline_price
total_diesel = fuel_amount * diesel_price
total_gas = fuel_amount * gas_price

if 20 <= fuel_amount <= 25:
    total_gasoline = total_gasoline - 0.08 * total_gasoline
    total_diesel = total_diesel - 0.08 * total_diesel
    total_gas = total_gas - 0.08 * total_gas
elif fuel_amount > 25:
    total_gasoline = total_gasoline - 0.1 * total_gasoline
    total_diesel = total_diesel - 0.1 * total_diesel
    total_gas = total_gas - 0.1 * total_gas

if type_of_fuel == "Gasoline":
    print(f"{total_gasoline:.2f} lv.")
elif type_of_fuel == "Diesel":
    print(f"{total_diesel:.2f} lv.")
elif type_of_fuel == "Gas":
    print(f"{total_gas:.2f} lv.")


