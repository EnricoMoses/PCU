my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict_items_view = my_dict.items()
print(dict_items_view)

# Iterating through the items
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# # Demonstrating dynamic update
# my_dict['age'] = 31
# print(dict_items_view)  # The view object reflects the change