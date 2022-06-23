def fire(index, damage):
    if index in range(0, len(warship)):
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            return True


def defend(start_index, end_index, damage):
    if 0 <= start_index <= len(pirate_ship) - 1 and 0 < end_index <= len(pirate_ship) - 1:
        for section in range(start_index, end_index + 1):
            pirate_ship[section] -= damage
            if pirate_ship[section] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                return True


def repair(index, health):
    if 0 <= index <= len(pirate_ship) - 1:
        pirate_ship[index] += health
        if pirate_ship[index] > section_capacity:
            pirate_ship[index] = section_capacity


def status(pirates):
    need_repair = []
    for i in range(0, len(pirates)):
        if pirates[i] < section_capacity * 0.2:
            need_repair.append(pirates[i])
    print(f"{len(need_repair)} sections need repair.")


pirate_ship = [int(el) for el in input().split(">")]
warship = [int(el) for el in input().split(">")]
section_capacity = int(input())
command = input()
while command != "Retire":
    current = command.split()
    order = current[0]
    if order == "Fire":
        index = int(current[1])
        damage = int(current[2])
        if fire(index, damage):
            break
    elif order == "Defend":
        start = int(current[1])
        end = int(current[2])
        damage = int(current[3])
        if defend(start, end, damage):
            break
    elif order == "Repair":
        index = int(current[1])
        health = int(current[2])
        repair(index, health)
    elif order == "Status":
        status(pirate_ship)
    command = input()
else:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
