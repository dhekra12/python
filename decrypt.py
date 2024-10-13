import string
def decrypt (message, shift):
    alphabet = string.ascii_lowercase
    decrypt_message =""
    for letter in message:
        if letter.lower() in alphabet:
            original_index= alphabet.index(letter.lower())
            new_position= (original_index - shift) % 26
            decrypt_letter= alphabet[new_position]
            if letter.isupper():
                decrypt_letter=decrypt_letter.upper()
            decrypt_message+= decrypt_letter
        else:
            decrypt_message+= letter
    print(
    f"\n\nHere is the original message\n*****\n\n{decrypt_message}\n\n*****"
)
    
user_message = input("Enter a message:")
shift_number = int(input("Enter a shift number: "))
decrypt(user_message, shift_number)
                