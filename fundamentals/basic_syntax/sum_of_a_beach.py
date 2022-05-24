user_input = input().lower()
counter = 0
for i in range(1, len(user_input) + 1):
    current_word = user_input[:i]
    if "sand" in current_word:
        counter += 1
        user_input = user_input[len(current_word):]
    elif "water" in current_word:
        counter += 1
        user_input = user_input[len(current_word):]
    elif "fish" in current_word:
        counter += 1
        user_input = user_input[len(current_word):]
    elif "sun" in current_word:
        counter += 1
        user_input = user_input[len(current_word):]
print(counter)
