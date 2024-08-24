alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_text,shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#                                                     # in this line we are adding the shift amount to the index of the letter in the alphabet list
#                                                     # we then use the modulo operator to get the remainder of the division of the shifted position by the length of the alphabet
#                                                     # this is because the index of the letter in the alphabet list is the position of the letter in the alphabet
#         cipher_text += alphabet[shifted_position]
        
#     print(f"The encoded text is {cipher_text}")
    
# encrypt(original_text=text,shift_amount=shift)
        

# def decrypt(cipher_text,shift_amount):
#     original_text = ""
#     for letter in cipher_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         original_text += alphabet[shifted_position]
        
#     print(f"The decoded text is {original_text}")
    
# decrypt(cipher_text=text,shift_amount=shift)

def caesar(original_text,shift_amount,encode_or_decode):
    output = " "
    
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output += alphabet[shifted_position]
        
    print(f"The {encode_or_decode}d text is {output}")
    
caesar(original_text = text,shift_amount = shift,encode_or_decode = direction)