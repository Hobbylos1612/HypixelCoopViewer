import requests
# Config
Apikey = "b232d270-6e92-4ca9-a3dc-9e426c084ddd"
#-------- TESTING --------
username = "prinesti"
#-------- TESTING --------
#-------- Uuid --------
Uuid_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
Uuid_response = requests.get(Uuid_url)
uuid = Uuid_response.json()["id"]
#-------- Uuid --------

# URL of the Hypixel API
url = "https://api.hypixel.net/player"
# Parameters
params = {
    "key": Apikey,
    "uuid": uuid
}

response = requests.get(url, params=params)
data = response.json()
uuid_Profiles = data["player"]["stats"]["SkyBlock"].get("profiles", {})
cute_names = [profile.get("cute_name") for profile in uuid_Profiles.values()]
print(cute_names)
print(f"1-{len(cute_names)}")
Choice = int(input("Select a profile by number: ").strip()) - 1
selected_cute_name = cute_names[Choice]
selected_profile_id = None
for profile in uuid_Profiles.values():
    if profile.get("cute_name") == selected_cute_name:
        profile_id = profile.get("profile_id").replace("-", "")
        break
print(profile_id)
print("1a475bf6677e4b4eb006aebe6b6d0875")