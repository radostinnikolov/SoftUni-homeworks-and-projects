number_of_days = int(input())
hours_for_each_day = int(input())
total_overall = 0
day_counter = 0
for day in range(1, number_of_days + 1):
    if day % 2 != 0:
        day_counter += 1
        total_for_day = 0
        tax = 0
        for hour in range(1, hours_for_each_day + 1):
            if hour % 2 == 0:
                tax = 1.25
                total_for_day += tax
            else:
                tax = 1
                total_for_day += tax
        total_overall += total_for_day
        print(f"Day: {day_counter} - {total_for_day:.2f} leva")
        continue
    if day % 2 == 0:
        day_counter += 1
        total_for_day = 0
        tax = 0
        for hour in range(1, hours_for_each_day + 1):
            if hour % 2 != 0:
                tax = 2.50
                total_for_day += tax
            else:
                tax = 1
                total_for_day += tax
        total_overall += total_for_day
        print(f"Day: {day_counter} - {total_for_day:.2f} leva")
        continue
print(f"Total: {total_overall:.2f} leva")



