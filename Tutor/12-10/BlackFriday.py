n = int(input())
rolls = list(map(int, input().split()))

freq = {}
for r in rolls:
    freq[r] = freq.get(r, 0) + 1


unique_rolls = [r for r in rolls if freq[r] == 1]
if not unique_rolls:
    print("none")
else:
    max_unique = max(unique_rolls)
    print(rolls.index(max_unique) + 1)
