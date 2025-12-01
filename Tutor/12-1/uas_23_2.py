n = int(input())
share = input().split()

share_int = []
try:
    if len(share) != n:
        raise Exception('share harus sama dengan total video')
    for i in share:
        if int(i) < 0:
            raise Exception('Angka tidak boleh negatif')
        share_int.append(int(i))
except Exception as e:
    print(e)
else:
    share_int.sort(reverse=True)
    index = 1
    for i in share_int:
        if i >= index:
            index = index + 1
        elif i < index:
            break

    print(index -1)




