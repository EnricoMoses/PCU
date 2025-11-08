# try:
#     a = int(input())
#     b = int(input())
#     c = a/b
#     print(c)
# # except ValueError:
# #     print('error')
# except Exception as e:
#     print(e)
#
# print('selesai')

while True:
    try:
        a = int(input("Masukkan angka antara 10 dan 30: "))
        if a < 10:
            raise Exception('Input jangan dibawah 10')
        elif a > 30:
            raise Exception('Input jangan diatas 30')
        else:
            print("Input benar")
            break
    except Exception as e:
        print('Ada Error:', e)