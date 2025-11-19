#TODO: import package yang dibutuhkan untuk encrypt decrypt

# from cryptex_pkg.core.vigenere import encrypt, decrypt
from cryptex_pkg import encrypt, decrypt

def main():
    #TODO: Lengkapi kode sesuai dengan perintah soal
    text = input("Text: ")
    key = input("Key: ")

    encrypted = encrypt(text, key)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted:", decrypted)

    # pass # TODO: hapus ini setelah implementasi

if __name__ == "__main__":
    main()