def prepare_key(text: str, key: str) -> str:
    """
    Membuat key penuh untuk Vigenère Cipher berdasarkan jumlah huruf alfabet pada text.
    Spasi, angka, simbol tidak dihitung.

    Contoh:
        text = "Halo Dunia!"
        key = "JAGO"
        return "JAGOJAGOJ"
    """
    #TODO: Lengkapi kode ini
    if not key:
        raise ValueError("key tidak boleh kosong")

    key_full = []
    key_index = 0
    key_len = len(key)

    for ch in text:
        if ch.isalpha():
            key_char = key[key_index % key_len]
            key_full.append(key_char)
            key_index += 1

    return "".join(key_full)

    # pass  # TODO: hapus ini setelah implementasi