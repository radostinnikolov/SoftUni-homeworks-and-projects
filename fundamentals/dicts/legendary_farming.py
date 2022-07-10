materials = {'shards': 0, 'fragments': 0, 'motes': 0}

is_obtained = False
while True:
    all_materials = input().split()
    for i in range(0, len(all_materials), 2):
        quantity = int(all_materials[i])
        material = all_materials[i+1].lower()
        if material not in materials:
            materials[material] = 0
        materials[material] += quantity
        if materials['shards'] >= 250:
            print("Shadowmourne obtained!")
            materials['shards'] -= 250
            is_obtained = True
            break
        elif materials['fragments'] >= 250:
            print("Valanyr obtained!")
            materials['fragments'] -= 250
            is_obtained = True
            break
        elif materials['motes'] >= 250:
            print("Dragonwrath obtained!")
            materials['motes'] -= 250
            is_obtained = True
            break
    if is_obtained:
        break

for key, value in materials.items():
    print(f"{key}: {value}")