number_of_people = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_museum_tickets = int(input())
total_nights = 20 * number_of_nights
total_cards = 1.6 * number_of_transport_cards
total_museum = 6 * number_of_museum_tickets
total = (total_nights + total_cards + total_museum) * 1.25
end_total = total * number_of_people
print(f"{end_total:.2f}")