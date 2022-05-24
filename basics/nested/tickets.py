total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
command = input()
while command != "Finish":
    name_of_movie = command
    free_places = int(input())
    tickets_sold = 0
    while free_places > tickets_sold:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        else:
            if type_of_ticket == "student":
                student_tickets += 1
            elif type_of_ticket == "standard":
                standard_tickets += 1
            elif type_of_ticket == "kid":
                kid_tickets += 1
        tickets_sold += 1
    total_tickets += tickets_sold
    percent_full = tickets_sold / free_places * 100
    print(f"{name_of_movie} - {percent_full:.2f}% full.")
    command = input()
percent_student = student_tickets / total_tickets * 100
percent_standard = standard_tickets / total_tickets * 100
percent_kid = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
