import itertools
import string

def brute_force_crack(password_to_crack, max_length=4):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    
    # Try every combination of characters up to the specified max length
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password_to_crack:
                print(f"Password cracked: {guess}")
                print(f"Attempts: {attempts}")
                return guess
    print("Password not cracked.")
    return None

# Example usage
password = "aBii"
brute_force_crack(password, max_length=4)
