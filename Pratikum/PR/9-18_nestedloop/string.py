s = input().lower()

vokal = 0
mati = 0
for i in s:
    if i in 'aiueo':
        if vokal < s.count(i):
            vokal = s.count(i)
    else:
        if mati < s.count(i):
            mati = s.count(i)

print(vokal+mati)


