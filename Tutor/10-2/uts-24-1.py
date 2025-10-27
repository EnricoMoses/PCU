suhu = float(input('Berapa suhu badan Anda? (dalam derajat Celcius): '))
tekanan_darah = input('Bagaimana tekanan darah Anda? (rendah/normal/tinggi): ')
batuk = input('Apakah Anda mengalami batuk? (ya/tidak):')
sesak_nafas = input('Apakah Anda mengalami sesak nafas? (ya/tidak):')
sakit_tenggorokan = input('Apakah Anda mengalami sakit tenggorokan? (ya/tidak):')
nyeri_otot = input('Apakah Anda mengalami nyeri otot? (ya/tidak):')
sakit_kepala = input('Apakah Anda mengalami sakit kepala? (ya/tidak):')
mual = input('Apakah Anda mengalami mual? (ya/tidak):')
pengliatan_kabur = input('Apakah Anda mengalami pengliatan? (ya/tidak):')
pusing = input('Apakah Anda mengalami pusing? (ya/tidak):')
diare = input('Apakah Anda mengalami diare? (ya/tidak):')

diagnosis = []


if batuk == 'ya' and sesak_nafas == 'ya' and suhu > 37.5 and (tekanan_darah == 'normal' or tekanan_darah == 'tinggi'):
    diagnosis.append('Pneumonia')
if batuk == 'ya' and sakit_tenggorokan == 'ya' and 37 < suhu < 37.5:
    diagnosis.append('Flue')
if batuk == 'ya' and nyeri_otot == 'ya' and suhu > 38.5:
    diagnosis.append('Demam Berdarah')

if sakit_kepala == 'ya' and mual == 'ya' and pengliatan_kabur == 'ya':
    diagnosis.append('Migrain')
if sakit_kepala == 'ya' and pusing == 'ya' and tekanan_darah == 'rendah':
    diagnosis.append('Vertigo')

if diare == 'ya' and mual == 'ya' and 36 < suhu < 37.5:
    diagnosis.append('Keracunan Makanan')
if diare == 'ya' and suhu > 37.5:
    diagnosis.append('Infeksi Usus')

if diagnosis:
    print(f'Diagnosis awal: {", ".join(diagnosis)}')
else:
    print('Penyakit tidak ditemukan')
