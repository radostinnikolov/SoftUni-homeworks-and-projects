cards = input().split(" ")
number_of_shuffles = int(input())
length = len(cards)

shuffled_deck = []
for shuffle in range(number_of_shuffles):
    left_part = cards[:length // 2]
    right_part = cards[length // 2:]
    for i in range(len(left_part)):
        shuffled_deck.append(left_part[i])
        shuffled_deck.append(right_part[i])
    cards = shuffled_deck
    shuffled_deck = []
print(cards)