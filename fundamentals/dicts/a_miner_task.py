miner_dict = {}
command = input()
while command != 'stop':
    resource = command
    amount = int(input())
    if resource not in miner_dict:
        miner_dict[resource] = 0
    miner_dict[resource] += amount
    command = input()
for key, value in miner_dict.items():
    print(f"{key} -> {value}")