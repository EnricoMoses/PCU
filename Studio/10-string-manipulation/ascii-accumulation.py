input_s = input().lower()

total = 0
for kata in input_s:
    total += ord(kata)
print(total)