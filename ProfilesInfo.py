import requests
# URL of the Hypixel API
url_profile = "https://api.hypixel.net/v2/skyblock/profile"
profile_id = "1a475bf6677e4b4eb006aebe6b6d0875"
Coop_Members = []
Apikey = "b232d270-6e92-4ca9-a3dc-9e426c084ddd"
# Parameters
params_profile = {
    "key": Apikey,
    "profile": profile_id
}
# Make the request with query parameters
response_profile = requests.get(url_profile, params=params_profile)
data_profile = response_profile.json()
profilesMembers = data_profile["profile"].get("members", {})
profile_Uuids = list(profilesMembers.keys())
for uuids in profile_Uuids:
    Api = f"https://api.hypixel.net/player?uuid={uuids}&key={Apikey}"
    Api_responese = requests.get(Api)
    Apidata = Api_responese.json()
    uuid_Profiles = Apidata["player"]["stats"]["SkyBlock"].get("profiles", {})
    UserName = Apidata["player"]["displayname"]
    uuid_profile_ids = list(uuid_Profiles.keys())
    if profile_id in uuid_profile_ids:
        Coop_Members.append(UserName)
print("\n".join(Coop_Members))
