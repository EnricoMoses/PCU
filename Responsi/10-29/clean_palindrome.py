def clean_palindrome(s):
    s = s.lower()

    if len(s) <= 1:
        return True

    if not s[0].isalnum():
        return clean_palindrome(s[1:])

    if not s[-1].isalnum():
        return clean_palindrome(s[:-1])

    if s[0] != s[-1]:
        return False

    return clean_palindrome(s[1:-1])

print(clean_palindrome("Kasur ini rUsak!"))       # -> True
print(clean_palindrome("A man, a plan, a canal: Panama"))  # -> True
print(clean_palindrome("hello"))                    # -> False
print(clean_palindrome(""))   # -> True
