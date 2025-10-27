number = int(input('Masukkan nilai number (n): '))

given_number = number
generated_number = 0
while given_number > 0:
    digit = given_number % 10
    given_number //= 10
    generated_number = generated_number * 10 + digit

if generated_number == number:
    print('Palindrome')
else:
    print('Not Palindrome')