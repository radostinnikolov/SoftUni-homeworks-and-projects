searched_book = input()
counter = 0
current_book = input()
while current_book != "No More Books":
    if current_book == searched_book:
        break
    current_book = input()
    counter += 1
if current_book == searched_book:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")