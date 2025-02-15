import requests
import json

URL = "http://localhost:8080/api/notes"  # Ensure the correct API path

new_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ0FBQUFBQm5yM0E4UWp4N3JSbi0xRy1jTDZpOWx2TXVfVF9sVEtQdnFUS3NpbWN2Z0J4VUJjX1NzdnMwbUxhcjEwUFFsUWxUWnNyWS1uWUpFaW9vZXF6V3JTOTBYV1ZpNnc9PSIsImV4cCI6MTczOTU1MjQwMH0.qxg1MjLrvw5xcTCzzkyhdhE4u2MCp1_phsJS5EiJuWc"

headers = {
    "Authorization": "Bearer " + new_token
}

response = requests.get(URL, headers=headers)

print("Response:", response.text)

