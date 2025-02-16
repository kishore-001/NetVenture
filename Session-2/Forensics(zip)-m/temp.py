# Read the ZIP file and convert to binary text
zip_filename = "challenge.zip"  # Change this to your actual ZIP file name
output_txt = "upsidedown.txt"

with open(zip_filename, "rb") as zip_file:
    binary_data = zip_file.read()  # Read binary data
    binary_text = ''.join(format(byte, '08b') for byte in binary_data)  # Convert to binary string

# Save the binary output to a text file
with open(output_txt, "w") as text_file:
    text_file.write(binary_text)

print(f"Binary-coded text saved to {output_txt}")
