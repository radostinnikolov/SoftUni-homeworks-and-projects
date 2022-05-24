number_of_groups = int(input())
p1_mus = 0
p2_mon = 0
p3_kil = 0
p4_k2 = 0
p5_eve = 0
total_people = 0
for i in range(number_of_groups):
    people_per_group = int(input())
    total_people += people_per_group
    if people_per_group <= 5:
        p1_mus += people_per_group
    elif people_per_group <= 12:
        p2_mon += people_per_group
    elif people_per_group <= 25:
        p3_kil += people_per_group
    elif people_per_group <= 40:
        p4_k2 += people_per_group
    elif people_per_group > 40:
        p5_eve += people_per_group
percent_p1 = p1_mus / total_people * 100
percent_p2 = p2_mon / total_people * 100
percent_p3 = p3_kil / total_people * 100
percent_p4 = p4_k2 / total_people * 100
percent_p5 = p5_eve / total_people * 100
print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")