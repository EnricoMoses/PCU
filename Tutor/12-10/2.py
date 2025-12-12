def hitung_p_index(shares):
    shares.sort(reverse=True)
    p_index = 0
    for i, s in enumerate(shares, start=1):
        if s >= i:
            p_index = i
        else:
            break
    return p_index

try:
    n = int(input("Jumlah posting: "))
    if n <= 0 or n > 100:
        raise ValueError("Jumlah posting harus antara 1 sampai 100.")

    shares_input = input("Jumlah sharing per posting (pisahkan dengan spasi): ").split()
    if len(shares_input) != n:
        raise ValueError(f"Jumlah sharing harus sebanyak {n} angka.")

    shares = []
    for s in shares_input:
        si = int(s)
        if si < 0:
            raise ValueError("Jumlah sharing tidak boleh negatif.")
        shares.append(si)

except ValueError as e:
    print("Input tidak valid:", e)
    exit()

p_index = hitung_p_index(shares)
print("p-index =", p_index)
