while True:
    try:
        jumlah_tiket = int(input('Masukkan jumlah tiket: '))
        if jumlah_tiket <= 0:
            raise Exception('Jumlah tiket tidak boleh kurang dari 1')
        if jumlah_tiket > 4:
            raise Exception('Jumlah tiket tidak boleh lebih dari 4')
        harga_tiket = 500_000
        total = harga_tiket * jumlah_tiket
        print('Total harga tiket : ', total)
        break


    except ValueError:
        print('Input harus berupa angka')
    except Exception as e:
        print('Error: ', e)