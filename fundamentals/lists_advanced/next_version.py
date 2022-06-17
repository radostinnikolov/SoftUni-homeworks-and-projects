version = [int(el) for el in input().split(".")]
version[-1] += 1
if version[-1] == 10:
    version[-1] = 0
    version[-2] += 1
    if version[-2] == 10:
        version[-2] = 0
        version[-3] += 1
print(".".join(str(el) for el in version))