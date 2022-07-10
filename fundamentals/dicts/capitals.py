countries = input().split(', ')
capitals = input().split(', ')
my_dict = {country: capital for country, capital in zip(countries, capitals)}
for key, value in my_dict.items():
    print(f"{key} -> {value}")