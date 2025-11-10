cards = ['5M', '7K', '8B', '7S', '0B']

urutan_angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
urutan_simbol = ['K', 'M', 'B', 'S']

sorted_cards = []

# for i in range(len(cards)):
#     highest = '1K'
#     for i in cards:
#         if urutan_angka.index(highest[0]) < urutan_angka.index(i[0]):
#             highest = i
#         elif urutan_angka.index(highest[0]) == urutan_angka.index(i[0]):
#             if urutan_simbol.index(highest[1]) < urutan_simbol.index(i[1]):
#                 highest = i
#
#     cards.remove(highest)
#     sorted_cards.append(highest)
#
# print(sorted_cards)


def card_sorting(cards, sorted_cards):
    if len(cards) == 0:
        return

    highest = '1K'
    for i in cards:
        if urutan_angka.index(highest[0]) < urutan_angka.index(i[0]):
            highest = i
        elif urutan_angka.index(highest[0]) == urutan_angka.index(i[0]):
            if urutan_simbol.index(highest[1]) < urutan_simbol.index(i[1]):
                highest = i

    cards.remove(highest)
    sorted_cards.append(highest)
    card_sorting(cards, sorted_cards)


card_sorting(cards, sorted_cards)

print(sorted_cards)