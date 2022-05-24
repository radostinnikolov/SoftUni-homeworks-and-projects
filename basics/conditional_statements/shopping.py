budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_price = 250
cpu_price = 0.35 * gpu_price * gpu_amount
ram_price = 0.1 * gpu_price * gpu_amount
total = gpu_price * gpu_amount + cpu_price * cpu_amount + ram_price * ram_amount

if gpu_amount > cpu_amount:
    total *= 0.85

if total > budget:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
else:
    print(f"You have {abs(total - budget):.2f} leva left!")
