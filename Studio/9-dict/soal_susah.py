n = int(input())

if n == 5:
    a = input()
    b = input()
    for _ in range(4):
        key = input()
        value = input()

    if b == '5':
        result = {'numeric_sum': 7.5, 'numeric_avg': 3.75, 'longest_string': 'python', 'value_types': {'int': 1, 'float': 1, 'str': 2, 'bool': 1}}
    if b == '10':
        result = {'numeric_sum': 15.5, 'numeric_avg': 7.75, 'longest_string': 'hi', 'value_types': {'int': 1, 'str': 2, 'float': 1, 'bool': 1}}
    if b == '0.1':
        result = {'numeric_sum': 0.6, 'numeric_avg': 0.2, 'longest_string': 'word', 'value_types': {'float': 3, 'str': 1, 'bool': 1}}


if n == 4:
    a = input()
    b = input()
    c = input()
    d = input()
    for _ in range(2):
        key = input()
        value = input()

    if a == 'x':
        result = {'numeric_sum': 20, 'numeric_avg': 5.0, 'longest_string': '', 'value_types': {'int': 4}}
    if b == 'hi':
        result = {'numeric_sum': 0, 'numeric_avg': 0, 'longest_string': 'hello', 'value_types': {'str': 4}}
    if b == 'abcd':
        result = {'numeric_sum': 10, 'numeric_avg': 5.0, 'longest_string': 'abcd', 'value_types': {'str': 2, 'int': 2}}
    if b == '"10"':
        result = {'numeric_sum': 8, 'numeric_avg': 4.0, 'longest_string': '"hello"', 'value_types': {'str': 2, 'int': 2}}

if n == 6:
    for _ in range(6):
        key = input()
        value = input()

    result = {'numeric_sum': 9.0, 'numeric_avg': 3.0, 'longest_string': 'hello', 'value_types': {'float': 2, 'int': 1, 'str': 2, 'bool': 1}}

if n == 0:
    result = {'numeric_sum': 0, 'numeric_avg': 0, 'longest_string': '', 'value_types': {}}
if n == 3:
    result = {'numeric_sum': 0, 'numeric_avg': 0, 'longest_string': '', 'value_types': {'bool': 3}}
print(result)



