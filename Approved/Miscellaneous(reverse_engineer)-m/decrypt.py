def decrypt_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        encrypted_text = file.read().strip()

    decrypted_chars = []
    
    for char in encrypted_text:
        high = chr(ord(char) >> 8)  # Extract the high byte
        low = chr(ord(char) & 0xFF)  # Extract the low byte
        decrypted_chars.append(high + low)

    return "".join(decrypted_chars)

# Example usage
file_path = "challenge.enc"  # Replace with the actual file name
decrypted_text = decrypt_from_file(file_path)
print("Decrypted Text:", decrypted_text)
