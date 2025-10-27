bilangan1 = float(input('Masukkan bilangan 1: '))
bilangan2 = float(input('Masukkan bilangan 2: '))
bilangan3 = float(input('Masukkan bilangan 3: '))
operator1 = str(input('Masukkan operator aritmatika pertama (+,-,*,/): '))
operator2 = str(input('Masukkan operator aritmatika kedua (+,-,*,/): '))

isNotDividable = False
match operator1, operator2:
    case ('+'|'-'|'*'|'/'), ('+'|'-'|'*'|'/'):
        match operator1:
            case '+':
                hasil = bilangan1 + bilangan2
            case '-':
                hasil = bilangan1 - bilangan2
            case '*':
                hasil = bilangan1 * bilangan2
            case '/':
                if bilangan2 == 0:
                    isNotDividable = True
                else:
                    hasil = bilangan1 / bilangan2

        if not isNotDividable:
            match operator2:
                case '+':
                    hasil = hasil + bilangan3
                case '-':
                    hasil = hasil - bilangan3
                case '*':
                    hasil = hasil * bilangan3
                case '/':
                    if bilangan3 == 0:
                        isNotDividable = True
                    else:
                        hasil = hasil / bilangan3

        if isNotDividable:
            print('Operasi gagal dilakukan')
        else:
            print(f'Hasil: {hasil}')

    case _ :
        print('Input tidak valid')