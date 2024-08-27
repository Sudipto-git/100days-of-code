alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

caeser_art = ["""                                                                  
 ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8  
8b          ,adPPPPP88  8PP"""""""   `"Y8ba,   ,adPPPPP88  88          
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88          
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88          
                                                                  
                                                                  """]


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
    
    if encode_or_decode == "decode":
            shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            output += letter
            
        else:
        
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]
        
    print(f"The {encode_or_decode}d text is {output}")
    print(caeser_art[0])
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text = text,shift_amount = shift,encode_or_decode = direction)
    
    again = input("You want to do it again? Type 'yes' or 'no'\n").lower()
    
    if again == "no":
        should_continue = False
        print("Goodbye")
        
    