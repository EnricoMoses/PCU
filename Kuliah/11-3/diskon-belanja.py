try:
    total_belanja = int(input('Total belanja : '))
    print('''G = Gold → 20% 
S = Silver → 10% 
N = Non → 0% ''')
    member = input('Member : ')
    if member == 'G':
        total = total_belanja - total_belanja*0.2
    elif member == 'S':
        total = total_belanja - total_belanja*0.1
    elif member == 'N':
        total = total_belanja - total_belanja*0
    else:
        raise Exception('Member tidak valid')

except ValueError:
    print('Input harus angka')
except Exception as e:
    print(e)
else:
    print('Total: ', total)


