def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Upper/Lower case handle karne ke liye ASCII base standard
            ascii_offset = 65 if char.isupper() else 97
            # Caesar Cipher Math Formula: (x + n) % 26
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += new_char
        else:
            # Spaces aur Punctuation marks ko ignore nahi balkay waisa hi rakhenge
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            # Reverse Shift Logic: (x - n) % 26
            new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

# --- Program Execution Interface ---
if __name__ == "__main__":
    print("==================================================")
    print("      DECODELABS CAESAR CIPHER TOOL (PROJECT 2)   ")
    print("==================================================")
    
    # Input Data
    user_text = input("Enter Plaintext: ")
    shift_key = int(input("Enter Shift Key (e.g., 3): "))
    
    # Processing
    encrypted = caesar_encrypt(user_text, shift_key)
    decrypted = caesar_decrypt(encrypted, shift_key)
    
    # Display Output
    print("\n--- OUTPUT BREAKDOWN ---")
    print(f"Original Text:  {user_text}")
    print(f"Encrypted Text: {encrypted}")
    print(f"Decrypted Text: {decrypted}")
    print("==================================================")
