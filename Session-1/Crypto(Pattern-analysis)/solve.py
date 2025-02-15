import pprint

# Load the encrypted flag
file_path = "flag.enc"
with open(file_path, "rb") as f:
    encrypted_bytes = f.read()

# Convert bytes to hex representation
bytes_list = [hex(byte)[2:].zfill(2) for byte in encrypted_bytes]

# Count occurrences of each hex value
occurrences = {}
for byte in bytes_list:
    occurrences[byte] = occurrences.get(byte, 0) + 1

# Print occurrences to help with frequency analysis
print("Hex Value Occurrences:")
pprint.pprint(occurrences)

# Interactive substitution process
substitutions = {}
while True:
    # Display the current state of the flag with known substitutions
    decoded_flag = ''.join(substitutions.get(b, '_') for b in bytes_list)
    print("\nCurrent Deciphered Flag:", decoded_flag)
    
    # Get user input
    byte_to_replace = input("Which hex byte do you want to replace? (Enter 'exit' to quit): ")
    if byte_to_replace == 'exit':
        break
    
    replacement_char = input("What is the replacement character? [a-zA-Z0-9_{}]: ")
    
    # Store substitution
    substitutions[byte_to_replace] = replacement_char
