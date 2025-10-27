bulan = int(input())
tanggal = int(input())

match (bulan, tanggal):
    case (x, y) if (x == 1 and 1 <= y <= 19) or (x == 12 and 22 <= y <= 31):
        print('Capricorn')
    case (x, y) if (x == 1 and 20 <= y <= 31) or (x == 2 and 1 <= y <= 18):
        print('Aquarius')
    case (x, y) if (x == 2 and 19 <= y <= 29) or (x == 3 and 1 <= y <= 20):
        print('Pisces')
    case (x, y) if (x == 3 and 21 <= y <= 31) or (x == 4 and 1 <= y <= 19):
        print('Aries')
    case (x, y) if (x == 4 and 20 <= y <= 31) or (x == 5 and 1 <= y <= 20):
        print('Taurus')
    case (x, y) if (x == 5 and 21 <= y <= 31) or (x == 6 and 1 <= y <= 20):
        print('Gemini')
    case (x, y) if (x == 6 and 21 <= y <= 31) or (x == 7 and 1 <= y <= 22):
        print('Cancer')
    case (x, y) if (x == 7 and 23 <= y <= 31) or (x == 8 and 1 <= y <= 23):
        print('Leo')
    case (x, y) if (x == 8 and 23 <= y <= 31) or (x == 9 and 1 <= y <= 22):
        print('Virgo')
    case (x, y) if (x == 9 and 23 <= y <= 31) or (x == 10 and 1 <= y <= 22):
        print('Libra')
    case (x, y) if (x == 10 and 23 <= y <= 31) or (x == 11 and 1 <= y <= 21):
        print('Scorpio')
    case (x, y) if (x == 11 and 22 <= y <= 31) or (x == 12 and 1 <= y <= 21):
        print('Sagittarius')