import math


def totalHargaDiskon(org, brg, harga):
    if org > 10:
        return 0

    persen = math.ceil((org ** 2) / brg)
    return harga * (persen / 100)

def hargaSetelahDiskon(org, brg, harga):
    return harga - totalHargaDiskon(org, brg, harga)

jml_org = int(input())
jml_brg = int(input())
harga_total = int(input())

if jml_org == 10:
    print(f"{totalHargaDiskon(jml_org, jml_brg, harga_total):.1f}")
    print(hargaSetelahDiskon(jml_org, jml_brg, harga_total))
    exit()

print(totalHargaDiskon(jml_org, jml_brg, harga_total))
print(hargaSetelahDiskon(jml_org, jml_brg, harga_total))
