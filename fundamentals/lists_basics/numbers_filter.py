n = int(input())
numbers = []
filtered = []
for i in range(n):
    number = int(input())
    numbers.append(number)
command = input()
if command == "even":
    filtered = [x for x in numbers if x % 2 == 0]
elif command == "odd":
    filtered = [x for x in numbers if x % 2 != 0]
elif command == "positive":
    filtered = [x for x in numbers if x >= 0]
elif command == "negative":
    filtered = [x for x in numbers if x < 0]
print(filtered)

