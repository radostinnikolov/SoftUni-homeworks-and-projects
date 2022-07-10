result_dict = {}
n = int(input())
for i in range(n):
    key = input()
    synonym = input()
    if key not in result_dict:
        result_dict[key] = [synonym]
    else:
        if synonym not in result_dict[key]:
            result_dict[key].append(synonym)
for key, value in result_dict.items():
    print(f"{key} - {', '.join(value)}")
