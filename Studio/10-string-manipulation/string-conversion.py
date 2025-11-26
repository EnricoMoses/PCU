# input_s = list(input())
#
# hasil = []
# for i in range(len(input_s)):
#     if i % 2 == 0:
#         try:
#             hasil.append(input_s[i+1]*int(input_s[i]))
#         except:
#             hasil.append(input_s[i+2]*int(input_s[i] + input_s[i+1]))
#
# print(''.join(hasil))
#

s = input().strip()

# jika input kosong, langsung keluarkan string kosong
if s == "":
    print("")
else:
    hasil = []
    i = 0
    n = len(s)

    while i < n:
        # kumpulkan semua digit mulai dari posisi i
        if s[i].isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1

            # angka dari substring s[i:j]
            jumlah = int(s[i:j])

            # setelah digit, seharusnya ada 1 huruf
            if j < n:
                huruf = s[j]
                hasil.append(huruf * jumlah)

            # lanjut ke setelah huruf
            i = j + 1
        else:
            # kalau ada karakter non digit yang nyasar
            i += 1

    print("".join(hasil))
