p = 7919  # Prime
g = 7  # Generator
A = 5140  # Alice's public key
B = 987  # Bob's public key

# Brute-force private key 'a' by solving g^a ≡ A (mod p)
for a in range(1, p):
    if pow(g, a, p) == A:
        print(f"Found private key a: {a}")
        shared_secret = pow(B, a, p)
        print(f"Shared Secret: {shared_secret}")
        print(f"Flag: utflag{{{shared_secret}}}")
        break
