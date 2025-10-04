import requests
import pendulum
username = "prinesti"
Uuid_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
Uuid_response = requests.get(Uuid_url)
uuid = Uuid_response.json()["id"]
# URL of the Hypixel API
url = "https://api.hypixel.net/player"
# Parameters
params = {
    "key": "b232d270-6e92-4ca9-a3dc-9e426c084ddd",
    "uuid": uuid
}
# Make the request with query parameters
response = requests.get(url, params=params)
# Convert response to JSON
data = response.json()


# Getting the profiles and putting them in a list
profiles = data["player"]["stats"]["SkyBlock"].get("profiles", {})
profile_ids = list(profiles.keys())

# The profile_id i want to compare
target_profile_id = "1a475bf6677e4b4eb006aebe6b6d0875"

# Check if the profile exists
if target_profile_id in profiles:
    same_profile = True
    # Get the cute_name of the profile
    cute_name = profiles[target_profile_id].get("cute_name", "Unknown")
    print(f"Target profile exists: {same_profile}")
    print(f"Cute Name: {cute_name}")
else:
    same_profile = False
    print(f"Target profile exists: {same_profile}")
