import random

# Choose a small prime number and generator
p = 7919  # Small prime
g = 7  # Primitive root mod p

# Generate random private keys
a = random.randint(1000, 7000)  # Alice's private key
b = random.randint(1000, 7000)  # Bob's private key

# Compute public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Compute shared secret
S = pow(B, a, p)

# Generate the challenge
print(f"p = {p}")
print(f"g = {g}")
print(f"A = {A}")
print(f"B = {B}")
print(f"Flag: utflag{{{S}}}")  # Use S as the flag
