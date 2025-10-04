import requests
import pendulum
# Config
username = input("Enter PlayerName: ").strip()
profile_id = input("Enter profile_id: ").strip()
Toggle_SameProfile = False
Coop_Members = []
Apikey = "b232d270-6e92-4ca9-a3dc-9e426c084ddd"
#-------- TESTING --------
if not username:
    username = "prinesti"
if username == "prinesti" or "Goldenrune":
    profile_id = "1a475bf6677e4b4eb006aebe6b6d0875"
if username == "Arkcraftx":
    profile_id = "4dc02b88920448308e822756401cc81a"
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

params_profile = {
    "key": Apikey,
    "profile": profile_id
}

response = requests.get(url, params=params)
data = response.json()

#-------- LogIn and Logout --------
# LastLogIn
login_ms = data["player"].get("lastLogin", 0)
login = pendulum.from_timestamp(login_ms / 1000, tz="Europe/Berlin")
str_login = login.to_datetime_string()

# LastLogOut
logout_ms = data["player"].get("lastLogout", 0)
logoutAgo = pendulum.from_timestamp(logout_ms / 1000, tz="Europe/Berlin")
str_logoutAgo = logoutAgo.to_datetime_string()
#-------- LogIn and Logout --------

# Print result
playername = data["player"]["displayname"]
status = "ONLINE" if login_ms > logout_ms else "OFFLINE"
print(f"Player name: {playername}")
print(f"Status: {status}")
print(f"LastlogIn: {str_login}")
print(f"LastlogOutDiff: {logoutAgo.diff_for_humans()}")
print(f"LastlogOut: {str_logoutAgo}")

#-------- Same profile --------
if profile_id:
    profiles = data["player"]["stats"]["SkyBlock"].get("profiles", {})
    profile_ids = list(profiles.keys())


# Check if the profile exists
    if profile_id in profiles:
        same_profile = True
        # Get the cute_name of the profile
        cute_name = profiles[profile_id].get("cute_name", "Unknown")
        print(f"Target profile exists: {same_profile}")
        print(f"Cute Name: {cute_name}")
    else:
        same_profile = False
        print(f"Target profile exists: {same_profile}")
#-------- Same profile --------

#-------- Coop Members --------
    print("Coop Members: ")
    url_profile = "https://api.hypixel.net/v2/skyblock/profile"
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
    Coop_Members.remove(playername)
    print("\n".join(Coop_Members))
#-------- Coop Members --------
