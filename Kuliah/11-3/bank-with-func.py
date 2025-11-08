class SaldoError(Exception):
    pass

def tampilkan_menu():
    print('''=== MENU BANK MINI ===
1. Input saldo awal
2. Menabung
3. Mengambil uang
4. Menampilkan saldo
5. Keluar''')

def input_saldo_awal(saldo_sekarang: int) -> int:
    saldo_awal = int(input('Saldo awal: '))
    if saldo_awal < 0:
        raise Exception('Saldo awal tidak boleh negatif')
    return saldo_awal

def menabung(saldo_sekarang: int) -> int:
    tabung = int(input('Saldo menabung: '))
    if tabung < 0:
        raise Exception('Saldo  tidak boleh negatif')
    return saldo_sekarang + tabung

def mengambil_uang(saldo_sekarang: int) -> int:
    ambil = int(input('Saldo yg ingin di tarik: '))
    if ambil < 0:
        raise Exception('Saldo tidak boleh negatif')
    if ambil > saldo_sekarang:
        raise SaldoError('Anda menarik melebihi saldo anda')
    return saldo_sekarang - ambil

def tampilkan_saldo(saldo_sekarang: int) -> None:
    print('Saldo terakhir: ', saldo_sekarang)

def run():
    saldo = 0
    while True:
        try:
            tampilkan_menu()
            inp = input('Input: ')
            if inp == '1':
                saldo = input_saldo_awal(saldo)
            elif inp == '2':
                saldo = menabung(saldo)
            elif inp == '3':
                saldo = mengambil_uang(saldo)
            elif inp == '4':
                tampilkan_saldo(saldo)
            elif inp == '5':
                print('Keluar...')
                break
            else:
                raise Exception('Input harus diantara 1-5')

        except ValueError:
            print('Input harus berupa angka')
        except SaldoError as e:
            print('Error:', e)
        except Exception as e:
            print('Error:', e)

run()
