def morgan_string(jack, daniel):
    i = 0 # jack
    j = 0 # daniel
    n1 = len(jack)
    n2 = len(daniel)
    hasil = []

    while i < n1 or j < n2:
        if i == n1:
            hasil.append(daniel[j])
            j += 1
            continue

        if j == n2:
            hasil.append(jack[i])
            i += 1
            continue

        if jack[i] < daniel[j]:
            hasil.append(jack[i])
            i += 1
        elif jack[i] > daniel[j]:
            hasil.append(daniel[j])
            j += 1
        else:
            if jack[i:] <= daniel[j:]:
                hasil.append(jack[i])
                i += 1
            else:
                hasil.append(daniel[j])
                j += 1

    return ''.join(hasil)

jack = input().upper()
daniel = input().upper()
print(morgan_string(jack, daniel))