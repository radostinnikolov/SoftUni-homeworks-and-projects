people_in_parking_lot = {}
number_of_lines = int(input())
for i in range(number_of_lines):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        license_plate = command[2]
        if username not in people_in_parking_lot:
            people_in_parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command[0] == 'unregister':
        username = command[1]
        if username not in people_in_parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            people_in_parking_lot.pop(username)
for key, value in people_in_parking_lot.items():
    print(f"{key} => {value}")