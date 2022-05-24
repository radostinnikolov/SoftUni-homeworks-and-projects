queue = input()
queue_list = queue.split(sep=", ")
wolf_index = 0
for i in range(len(queue_list)):
    if queue_list[i] == "wolf":
        wolf_index = i
if wolf_index == len(queue_list) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(queue_list) - 1 - wolf_index}! You are about to be eaten by a wolf!")