def tribonacci(limit):
    total_seq = [1]
    for i in range(1, limit):
        if len(total_seq) > 2:
            total_seq.append(total_seq[i-3]+total_seq[i-2]+total_seq[i-1])
        else:
            total_seq.append(i)
    return total_seq


total_number = int(input())
print(*tribonacci(total_number))


