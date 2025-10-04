import requests
username = "roleplayeveryone"
Uuid_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
Uuid_response = requests.get(Uuid_url)
uuid = Uuid_response.json()["id"]
print(uuid)
