def check_for_force_side(force_side, force_book):
    if force_side in force_book:
        force_book[force_side].append(force_user)
    else:
        force_book[force_side] = [force_user]

force_book = {}

while True:
    book_input = input()
    if book_input == 'Lumpawaroo':
        break
    if '|' in book_input:
        book_input = book_input.split(' | ')
        force_side = book_input[0]
        force_user = book_input[1]
        for value in force_book.values():
            if force_user in value:
                break
        else:
            check_for_force_side(force_side, force_book)
    elif '->' in book_input:
        book_input = book_input.split(' -> ')
        force_side = book_input[1]
        force_user = book_input[0]
        for value in force_book.values():
            if force_user in value:
                value.remove(force_user)
                check_for_force_side(force_side, force_book)
                break
        else:
            check_for_force_side(force_side, force_book)
        print(f"{force_user} joins the {force_side} side!")

for key, value in force_book.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")

