input1 = input()
input2= int(input())
total = 0
sum_index = 0

for i, v in enumerate(input1):
    if int(v) + total < input2:
        total += int(v)
        sum_index += int(i)
    elif int(v) + total > input2:
        continue
    elif int(v) + total == input2:
        total += int(v)
        sum_index += int(i)
        print(sum_index)
        break
else:
    print('-1')