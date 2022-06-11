def palindrome_int(some_numbers):
    palindromes = []
    for num in some_numbers:
        if num == num[::-1]:
            palindromes.append(True)
            continue
        palindromes.append(False)
    return palindromes


numbers = input().split(", ")
for i in palindrome_int(numbers):
    print(i)