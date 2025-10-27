# Fungsi untuk hitung rata-rata
# Function menerima parameter list of numbers
# Function return hasil rata-rata
def average(numbers):
    # Jika list kosong, langsung return 0
    if not numbers:
        return 0

    # ambil total dari semua list menggunaakn method sum
    total = sum(numbers)
    # ambil panjang dari list menggunakan method len
    n = len(numbers)

    # hitung rata-rata dengan rumus total/n
    mean = total / n

    '''return mean lalu gunakan method round dan
    beri parameter keduanya 2 untuk menampilkan
    2 angka di belakang koma jika angka tersebut
    float
    '''
    return round(mean, 2)

# Test function

# hasil float
print(average([1, 2, 3, 4]))   # Output: 2.5
# list kosong akan menampilkan 0
print(average([]))             # Output: 0
# hasilnya bulat namun akan tetap ketampil dalam floatx
print(average([10, 20, 30]))   # Output: 20.0
