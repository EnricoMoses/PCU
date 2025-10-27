my_list = [8, 10, 6, 2, 4]
# list_string = input().split() # Menghasilkan list of string
# print(list_string)

# my_list = [int(i) for i in input().strip().split(' ')] # Menghasilkan list of integer
#
for i in range(len(my_list) - 1):
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)