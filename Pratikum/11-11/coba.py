data = {"Andi": 85,
        "Budi": 90,
        "Cici": 78}

# print(max(data.items()))                         # -> ('Cici', 78)  # dibandingkan berdasarkan nama ('Cici' alfabet terbesar)
# print(max(data.items(), key=lambda kv: kv[1]))   # -> ('Budi', 90)  # dibandingkan berdasarkan nilai
# print(max(data.values()))
# print(data.items())
# print(max(data.keys()))

for nama, nilai in data.items():
    print(nama, nilai)

print(data.items())