string_input = input()
indices = []
for index, char in enumerate(string_input):
    if char.isupper():
        indices.append(index)
print(indices)
