def chars_in_range(first_char, second_char):
    result_chars = []
    for char in range(ord(first_char) + 1, ord(second_char)):
        result_chars.append(chr(char))
    return result_chars


first = input()
second = input()
print(*chars_in_range(first, second))

