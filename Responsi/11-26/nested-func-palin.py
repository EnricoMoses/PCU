def longest_palindrome(s: str) -> str:
    # Fungsi bantu: kembangkan dari tengah (center) ke kiri dan kanan
    def expand_from_center(left: int, right: int) -> str:
        # Selama masih dalam batas dan huruf kiri = huruf kanan, terus meluas
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # substring palindrom yang terakhir valid adalah (left+1 : right)
        return s[left+1:right]

    if len(s) <= 1:
        return s

    longest = s[0]  # minimal 1 karakter pasti palindrom

    for i in range(len(s)):
        # Palindrom dengan panjang ganjil (tengah di satu karakter)
        odd = expand_from_center(i, i)
        if len(odd) > len(longest):
            longest = odd

        # Palindrom dengan panjang genap (tengah di antara dua karakter)
        even = expand_from_center(i, i + 1)
        if len(even) > len(longest):
            longest = even

    return longest


# ---- Program utama ----
text = input("Masukkan sebuah string: ")
result = longest_palindrome(text)
print("Substring palindrom terpanjang:", result)
