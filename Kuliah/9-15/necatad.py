# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print('*')

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print('#')

# var = 1
# while var < 10:
#     print('#')
#     var = var << 1

# z = 10
# y = 0
# print(y < z and z > y or y > z and z < y)

# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
#
# print(c + d + e)

# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])

# vals = [0,1,2]
# vals[0], vals[2] = vals[2], vals[0]

# vals = [0,1,2]
# vals.insert(0,1)
# del vals[1]
# print(vals)

# nums = [1,2,3]
# vals = nums
# del vals[1:2]
# print(vals)
# print(nums)

# nums = [1,2,3]
# vals = nums[-1:-2]
# print(vals)
# print(nums)

# my_list1 = [1, 2, 3]
# my_list2 = []
# for v in my_list1:
#     my_list2.insert(0, v)
# print(my_list2)

# my_list1 = [1, 2, 3]
# for v in range(len(my_list1)):
#     my_list1.insert(1, my_list1[v])
#     print(v)
#
# print(my_list1)

# my_list = [i for i in range(-1,2)]
# print(my_list)
#
# t = [[3-i for i in range(3)] for i in range(3)]
# s = 0
#
# print(t)
# for i in range(3):
#     s += t[i][i]
# print(s)

my_list = [[0,1,2,3] for i in range(2)]
print(my_list)