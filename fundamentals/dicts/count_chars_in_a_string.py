letters = input().split()
only_letters = "".join(letters)
letters_dict = {}
for letter in only_letters:
    if letter not in letters_dict:
        letters_dict[letter] = 0
    letters_dict[letter] += 1

for letter, value in letters_dict.items():
    print(f"{letter} -> {value}")
