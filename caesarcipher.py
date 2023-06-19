def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)


# Example usage
plaintext = "IcePopz infosec"
shift = 3

encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted Text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)
