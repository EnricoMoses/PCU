
# Versi
# kunci
# jawaban

data = {}
n = int(input())


def convert_value(v):
    # Coba convert ke bool
    if v == "True":
        return True
    if v == "False":
        return False

    # Coba convert ke integer
    try:
        return int(v)
    except:
        pass

    # Coba convert ke float
    try:
        return float(v)
    except:
        pass

    # Kalau gagal semua → string
    return v


for _ in range(n):
    k = input()
    v = convert_value(input())
    data[k] = v

numeric_values = []
string_values = []
type_count = {}

for v in data.values():
    t = type(v).__name__
    type_count[t] = type_count.get(t, 0) + 1

    if isinstance(v, (int, float)) and not isinstance(v, bool):
        numeric_values.append(v)
    if isinstance(v, str):
        string_values.append(v)

numeric_sum = sum(numeric_values) if numeric_values else 0
numeric_avg = round(numeric_sum / len(numeric_values), 2) if numeric_values else 0
longest = max(string_values, key=len) if string_values else ""

result = {
    "numeric_sum": numeric_sum,
    "numeric_avg": numeric_avg,
    "longest_string": longest,
    "value_types": type_count
}

print(result)