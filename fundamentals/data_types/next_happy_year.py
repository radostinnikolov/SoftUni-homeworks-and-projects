year = int(input())
year_list = [x for x in str(year)]

while True:
    year_set = set(year_list)
    if len(year_set) == len(year_list):
        print(year)
        break
    else:
        year += 1
        year_list = [x for x in str(year)]



