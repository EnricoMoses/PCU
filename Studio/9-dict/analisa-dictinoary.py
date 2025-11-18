n = int(input().strip())

numeric_sum = 0
numeric_count = 0
longest_string = ""
value_types = {}

for _ in range(n):
    key = input().strip()      # key dibaca tapi tidak dipakai
    raw = input().strip()      # value dalam bentuk string

    # tentukan tipe data value
    if raw == "True" or raw == "False":
        v_type = "bool"
        value = (raw == "True")
    else:
        try:
            value = int(raw)
            v_type = "int"
        except ValueError:
            try:
                value = float(raw)
                v_type = "float"
            except ValueError:
                value = raw
                v_type = "str"

    # catat jumlah tiap tipe data
    value_types[v_type] = value_types.get(v_type, 0) + 1

    # hitung numeric_sum dan numeric_count (hanya int & float)
    if v_type in ("int", "float"):
        numeric_sum += value
        numeric_count += 1

    # cari string terpanjang
    if v_type == "str" and len(value) > len(longest_string):
        longest_string = value

# hitung rata-rata numerik (dibulatkan 2 angka di belakang koma)
if numeric_count > 0:
    numeric_avg = round(numeric_sum / numeric_count, 2)
else:
    numeric_avg = 0

result = {
    "numeric_sum": numeric_sum,
    "numeric_avg": numeric_avg,
    "longest_string": longest_string,
    "value_types": value_types
}

print(result)
