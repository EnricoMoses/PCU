# my_list = [8, 10, 6, 2, 4]
#
# for i in range(len(my_list) - 1):
#     if my_list[i] > my_list[i + 1]:
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)

my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
#
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)

# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

board = [[i for i in range(8)] for j in range(8)]
print(board)