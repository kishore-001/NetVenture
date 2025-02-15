import jwt

fake_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ0FBQUFBQm5yM0E4UWp4N3JSbi0xRy1jTDZpOWx2TXVfVF9sVEtQdnFUS3NpbWN2Z0J4VUJjX1NzdnMwbUxhcjEwUFFsUWxUWnNyWS1uWUpFaW9vZXF6V3JTOTBYV1ZpNnc9PSIsImV4cCI6MTczOTU1MjQwMH0.lEyKRsN6UbY50jgiFhBhhQb3IAjNK9B890kZG5Yyy4E"

# Decode without verifying signature
decoded = jwt.decode(fake_token, options={"verify_signature": False})

print("Decoded JWT Payload:", decoded)
KEY = "H6jga21h1"  # Replace with the real secret key

# Re-sign the decoded payload
new_token = jwt.encode(decoded, KEY, algorithm="HS256")

print("New Signed Token:", new_token)

