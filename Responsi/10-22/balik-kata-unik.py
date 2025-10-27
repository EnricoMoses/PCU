# Function balik kata
# membalik urutan huruf tiap kata dalam kalimat, tapi urutan katanya tetap.
# membutuhkan parameter string yang berisi sebuah kalimat
# akan me return string yang membalik urutan kata tsb
def reverse_words(kalimat):
    # pecah kalimat menjadi kata dalam string
    words = kalimat.split()

    # balik tiap kata dengan slicing [::-1] menggunakan list comprehension
    reversed_kata = [w[::-1] for w in words]

    '''Gabungkan kembali kata menjadi kalimat
    Gabungkan list menjadi string dengan pemisah spasi
    '''
    return ' '.join(reversed_kata)

# Test Function
print(reverse_words("Aku suka Python"))
# Output: "ukA akus nohtyP"

print(reverse_words("Belajar coding seru"))
# Output: "rajaleB gnidoc ures"


