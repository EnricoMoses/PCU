username_benar = 'admin'
password_benar = '1234'

while True:
    try:
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')
        if username_benar == username and password == password:
            print('Login Berhasil')
            break
        if username == '' or password == '':
            raise Exception('Input tidak boleh kosong')
        if username_benar != username or password != password:
            print('Login Gagal')
            break
    except Exception as e:
        print('Error:', e)

