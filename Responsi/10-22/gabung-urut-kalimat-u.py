# Function untuk menggabungkan dan mengurutkan kalimat unik

# menerima parameter list of sentense(kallimat)
# menggambil seluruh kata yang unik dari seluruh kalimat
# menghapus duplikat
# mengurutkan berdasarkan pendek -> panjang, jika sama urutkan dari alfabet
# mereturn list dari hasil kata-kata tersebut

def merge_and_sort_words(sentenses):
    # Siapkan list kosong untuk menampung kata unik
    unique_words = []

    # gunakan loop untuk memecah kalimat dalam banyak kalimat
    for sentence in sentenses:
        # pecah kalimat menjadi list kata-kata
        words = sentence.split()

        # gunakan loop untuk memecah kata dari banyak kata-kata
        for word in words:
            # ubah semua ke huruf kecil agar konsisten dan akurat
            w = word.lower()

            # tambahkan hanya jika w belum ada di list unique_words
            if w not in unique_words:
                unique_words.append(w)

    '''
    Urutkan panjang list berdasarkan panjang kata dari kecil ke besar,
    jika panjang sama urutkan berdasarkan alfabet (w), gunakan method sort
    '''
    # urutkan alfabet terlebih dahulu dengan sort
    unique_words.sort()
    # lalu urutkan bedasarkan panjang
    unique_words.sort(key=len)


    # return list dari kata yang sudah di urutkan
    return unique_words

# test function
print(merge_and_sort_words(["Aku suka Python", "python itu keren", "Belajar itu seru"]))
# Output: ['aku', 'itu', 'seru', 'suka', 'keren', 'belajar', 'python']
