secret_message = [word for word in input().split()]
for word in secret_message:
    number = ""
    letters = ""
    for char in word:
        if char.isdigit():
            number += char
        else:
            letters += char
    first_letter = chr(int(number))
    if len(letters) < 2:
        rest_of_letters = letters[0]
    else:
        rest_of_letters = letters[-1] + letters[1:-1] + letters[0]
    current_deciphered_word = first_letter + rest_of_letters
    print(current_deciphered_word, end=" ")