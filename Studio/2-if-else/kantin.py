hari = input().lower()
jam = int(input())

menu = True
if hari == 'senin' :
    if 7 <= jam <= 9 :
        print('Roti bakar')
    elif 10 <= jam <= 13 :
        print('Nasi goreng')
    elif 14 <= jam <= 16 :
        print('Siomay')
    else :
        menu = False
elif hari == 'selasa':
    if 7 <= jam <= 10 :
        print('Pancake')
    elif 11 <= jam <= 14 :
        print('Spaghetti')
    elif 15 <= jam <= 16 :
        print('Jus alpukat')
    else:
        menu = False
elif hari == 'rabu':
    if 7 <= jam <= 10 :
        print('Bubur ayam')
    elif 11 <= jam <= 13 :
        print('Nasi goreng')
    elif 14 <= jam <= 16 :
        print('Telur gulung')
    else:
        menu = False
elif hari == 'kamis':
    if 7 <= jam <= 11 :
        print('Waffle')
    elif 12 <= jam <= 14 :
        print('Sate')
    elif 15 <= jam <= 16 :
        print('Salad')
    else:
        menu = False
elif hari == 'jumat':
    if 7 <= jam <= 9 :
        print('Roti bakar')
    elif 10 <= jam <= 14 :
        print('Spaghetti')
    elif 15 <= jam <= 16 :
        print('Jus alpukat')
    else :
        menu = False
else:
    menu = False

if not menu:
    print('Kantin sedang tutup')

