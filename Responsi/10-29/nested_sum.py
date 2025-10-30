def nested_sum(data):
    if not data:
        return 0

    head, tail = data[0], data[1:]

    if isinstance(head, int):
        return head + nested_sum(tail)

    if isinstance(head, list):
        return nested_sum(head) + nested_sum(tail)

print(nested_sum([1, [2, [3, 4], 5], 6]))
print(nested_sum([]))
print(nested_sum([[-1, 2], [3, [-4, 5]]]))

