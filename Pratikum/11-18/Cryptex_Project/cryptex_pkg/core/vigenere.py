#TODO: import function prepare key
from multiprocessing.spawn import prepare
from ..utils.key_manager import prepare_key

def encrypt(plain_text: str, key: str) -> str:
    """
    Enkripsi text menggunakan Vigenère Cipher.
    Hanya huruf (A-Z dan a-z) yang diproses, karakter lain dibiarkan.

    Rumus:
        E = (P + K) mod 26
    """
    #TODO: Lengkapi kode ini
    full_key = prepare_key(plain_text, key)
    result_chars = []
    key_index = 0

    for ch in plain_text:
        if ch.isalpha():
            k = full_key[key_index]
            key_index += 1

            p_num = ord(ch.upper()) - ord('A')
            k_num = ord(k.upper()) - ord('A')

            e_num = (p_num + k_num) % 26

            enc_char = chr(e_num + ord('A'))
            if ch.islower():
                enc_char = enc_char.lower()

            result_chars.append(enc_char)
        else:
            result_chars.append(ch)

    return "".join(result_chars)

def decrypt(cipher_text: str, key: str) -> str:
    """
    Dekripsi text Vigenère Cipher.
    Rumus:
        P = (E - K + 26) mod 26
    """
    #TODO: Lengkapi kode ini
    full_key = prepare_key(cipher_text, key)
    result_chars = []
    key_index = 0

    for ch in cipher_text:
        if ch.isalpha():
            k = full_key[key_index]
            key_index += 1

            e_num = ord(ch.upper()) - ord('A')
            k_num = ord(k.upper()) - ord('A')

            p_num = (e_num - k_num + 26) % 26

            dec_char = chr(p_num + ord('A'))
            if ch.islower():
                dec_char = dec_char.lower()

            result_chars.append(dec_char)
        else:
            result_chars.append(ch)

    return "".join(result_chars)
