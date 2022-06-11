def perfect_number(number):
    perfect_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            perfect_sum += divisor
    if perfect_sum == number:
        print("We have a perfect number!")
        return
    print("It's not so perfect.")




user_number = int(input())
perfect_number(user_number)