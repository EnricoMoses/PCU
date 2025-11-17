# # data = {}
# #
# # while True:
# #     nama = input('Masukkan Nama: ')
# #     if nama =='':
# #         break
# #
# #     nilai = int(input('Masukkan Nilai: '))
# #     if nilai not in range(0, 11):
# #         break
# #
# #     if nama in data:
# #         data[nama] += (nilai, )
# #     else:
# #         data[nama] = (nilai, )
# #
# #
# # print(data)
#
#
# # arr1 = [1,2,34,5]
# # arr2 = [1,2,34,5]
# #
# # print(arr1*2)
#
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
#
# for item in (d1, d2):
#     d3.update(item)
#
# print(d3)
#
# colors = (("green", "#008000"), ("blue", "#0000FF"))
#
# colors_dictionary = dict(colors)
# print(colors_dictionary)
#
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
# my_dictionary.clear()
del my_dictionary
print(copy_my_dictionary)
