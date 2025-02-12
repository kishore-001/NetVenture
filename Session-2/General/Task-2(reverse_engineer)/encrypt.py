def encrypt_and_store(flag, filename="challenge.enc"):
    # If the flag length is odd, append a null character '\x00' as padding
    if len(flag) % 2 != 0:
        flag += '\x00'

    # Encrypt the flag by packing two characters into one
    encrypted_text = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

    # Write encrypted data to the file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(encrypted_text)
    
    print(f"Encrypted data stored in {filename}")

# Example flag
flag = "MAGNUS{0x0r_1s_4m4z1ng}"
encrypt_and_store(flag)
