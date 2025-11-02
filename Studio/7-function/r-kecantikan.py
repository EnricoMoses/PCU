def kecantikan():
    return int(((B1*B2)+(B2/B4)) + B3)

def awetMuda():
    return int((B4+B3)*B1+B2)

def profit():
    return (awetMuda()+kecantikan())*2500


B1 = int(input())
B2 = int(input())
B3 = int(input())
B4 = int(input())

print(int(kecantikan()), int(awetMuda()), int(profit()))