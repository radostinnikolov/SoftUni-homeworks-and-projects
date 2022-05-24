change = float(input())
change_in_st = int(change * 100)
coins = 0
coins += change_in_st // 200
change_in_st %= 200
coins += change_in_st // 100
change_in_st %= 100
coins += change_in_st // 50
change_in_st %= 50
coins += change_in_st // 20
change_in_st %= 20
coins += change_in_st // 10
change_in_st %= 10
coins += change_in_st // 5
change_in_st %= 5
coins += change_in_st // 2
change_in_st %= 2
coins += change_in_st // 1
change_in_st %= 1
print(coins)


