Challenge Name: "Lost in Transmission"

Description:
The robots have introduced a new "secure" cryptographic system, claiming it to be unbreakable. However, you suspect it's just a standard Diffie-Hellman Key Exchange with small parameters. Your mission is to uncover their shared secret key and retrieve the hidden flag.

You are given the following public parameters:

    p: 7919
    g: 7
    A: 5140
    B: 987

Your task is to compute the shared secret between Alice and Bob. Once found, submit the flag in the format:

MAGNUS{shared_secret}