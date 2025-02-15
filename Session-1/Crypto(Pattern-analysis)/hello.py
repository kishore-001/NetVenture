import random

# Define the flag with the required format
flag = "magnus{manual_guessing_makes_a_fun_puzzle}"

# Generate a simple substitution cipher mapping
unique_bytes = random.sample(range(0x20, 0x7E), len(set(flag)))  # Unique non-control ASCII characters
cipher_map = {char: unique_bytes[i] for i, char in enumerate(set(flag))}

# Encrypt the flag using the substitution cipher
encrypted_flag = bytes([cipher_map[char] for char in flag])

# Save the encrypted flag to a file
file_path = "flag.enc"
with open(file_path, "wb") as f:
    f.write(encrypted_flag)

# Provide the cipher map (for challenge verification, not given to players)
cipher_map
