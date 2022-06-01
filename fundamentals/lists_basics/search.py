n = int(input())
key_word = input()
all_words = []
key_word_list = []
for strings in range(n):
    current = input()
    all_words.append(current)
    if key_word in current:
        key_word_list.append(current)
print(all_words)
print(key_word_list)