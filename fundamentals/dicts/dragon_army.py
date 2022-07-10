dragons_dict = {}
number_of_dragons = int(input())
for i in range(number_of_dragons):
    dragon_input = input().split()
    dragon_type = dragon_input[0]
    dragon_name = dragon_input[1]
    dragon_damage = dragon_input[2]
    dragon_health = dragon_input[3]
    dragon_armor = dragon_input[4]
    if dragon_damage == 'null':
        dragon_damage = 45
    else:
        dragon_damage = int(dragon_input[2])
    if dragon_health == 'null':
        dragon_health = 250
    else:
        dragon_health = int(dragon_input[3])
    if dragon_armor == 'null':
        dragon_armor = 10
    else:
        dragon_armor = int(dragon_input[4])

    if dragon_type not in dragons_dict:
        dragons_dict[dragon_type] = {}
    dragons_dict[dragon_type][dragon_name] = {'damage': dragon_damage, 'health': dragon_health, "armor": dragon_armor}

for key, value in dragons_dict.items():
    new_value = {name: dict_value for name, dict_value in sorted(value.items(), key=lambda x: x[0])}
    dragons_dict[key] = new_value

averages_dict = {}
for key in dragons_dict:
    averages_dict[key] = {}

for key, value in dragons_dict.items():
    damage = 0
    for name in value:
        damage += dragons_dict[key][name]['damage']
    averages_dict[key]['damage'] = damage / len(dragons_dict[key])
    health = 0
    for name in value:
        health += dragons_dict[key][name]['health']
    averages_dict[key]['health'] = health / len(dragons_dict[key])
    armor = 0
    for name in value:
        armor += dragons_dict[key][name]['armor']
    averages_dict[key]['armor'] = armor / len(dragons_dict[key])

for key, value in dragons_dict.items():
    print(f"{key}::({averages_dict[key]['damage']:.2f}/{averages_dict[key]['health']:.2f}/{averages_dict[key]['armor']:.2f})")
    for name in value:
        print(f"-{name} -> damage: {int(value[name]['damage'])}, health: {int(value[name]['health'])}, armor: {int(value[name]['armor'])}")





