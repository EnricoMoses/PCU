class SaldoError(Exception):
    pass

saldo = 0
while True:
    try:
        print('''=== MENU BANK MINI ===
1. Input saldo awal
2. Menabung
3. Mengambil uang
4. Menampilkan saldo
5. Keluar''')
        inp = input('Input: ')
        if inp == '1':
            try:
                saldo_awal = int(input('Saldo awal: '))
                if saldo_awal < 0:
                    raise Exception('Saldo awal tidak boleh negatif')
                saldo = saldo_awal
            except ValueError:
                print('Saldo awal harus berupa angka')
            except Exception as e:
                print('Error:', e)
        elif inp == '2':
            try:
                tabung = int(input('Saldo menabung: '))
                if tabung < 0:
                    raise Exception('Saldo  tidak boleh negatif')
                saldo += tabung
            except ValueError:
                print('Saldo awal harus berupa angka')
            except Exception as e:
                print('Error:', e)
        elif inp == '3':
            try:
                ambil = int(input('Saldo yg ingin di tarik: '))
                saldo -= ambil
                if saldo < 0:
                    raise Exception('Saldo tidak boleh negatif')
            except ValueError:
                print('Saldo harus berupa angka')
            except Exception as e:
                print('Error:', e)
        elif inp == '4':
            print('Saldo terakhir: ', saldo)
        elif inp == '5':
            print('Keluar...')
            break
        else:
            raise Exception('Input harus diantara 1-5')


    except ValueError:
        print('Input harus berupa angka')
    except Exception as e:
        print('Error:', e)