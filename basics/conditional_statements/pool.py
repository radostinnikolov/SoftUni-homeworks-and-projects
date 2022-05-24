volume_pool = int(input())
debit_pipe1 = int(input())
debit_pipe2 = int(input())
hours_missing = float(input())

water_pipe1 = debit_pipe1 * hours_missing
water_pipe2 = debit_pipe2 * hours_missing
water_liters = water_pipe1 + water_pipe2
percent_full = water_liters / volume_pool * 100
percent_pipe1 = water_pipe1 / water_liters * 100
percent_pipe2 = water_pipe2 / water_liters * 100

if water_liters > volume_pool:
    print(f"For {hours_missing} hours the pool overflows with {water_liters - volume_pool} liters.")
else:
    print(f"The pool is {percent_full}% full. Pipe 1: {percent_pipe1:.2f}%. Pipe 2: {percent_pipe2:.2f}%.")
