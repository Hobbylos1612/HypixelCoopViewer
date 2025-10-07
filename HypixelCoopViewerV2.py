import requests
import pendulum
# Config
username = input("Enter PlayerName: ").strip()
profile_search = True
Coop_Members = []
Apikey = "70de2484-b492-476e-8996-a1ce850888db"
cute_names = ()
profile_id = ""
#-------- TESTING --------
if not username:
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
playername = data["player"]["displayname"]
status = "ONLINE" if login_ms > logout_ms else "OFFLINE"

#-------- Profile Selector  --------
if profile_search:
    Profiles_data = data["player"]["stats"]["SkyBlock"].get("profiles", {})
    cute_names = [profile.get("cute_name") for profile in Profiles_data.values()]
    print(" ".join(cute_names))
    print(f"1-{len(cute_names)}")
    Choice = int(input("Select a profile by number: ").strip()) - 1
    selected_cute_name = cute_names[Choice]
    selected_profile_id = None
    for profile in Profiles_data.values():
        if profile.get("cute_name") == selected_cute_name:
            profile_id = profile.get("profile_id").replace("-", "")
            break
#-------- Profile Selector  --------
params_profile = {
    "key": Apikey,
    "profile": profile_id
}
#-------- Coop Members --------
if profile_search and not profile_id == "" :
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
#-------- Coop Members --------

# Print results
print("\n")
print("---------------------------------------------")
print(f"Player name: {playername}")
print(f"Status: {status}")
print(f"LastlogIn: {str_login}")
print(f"LastlogOutDiff: {logoutAgo.diff_for_humans()}")
print(f"LastlogOut: {str_logoutAgo}")
print("Profile Names: " + " ".join(cute_names))
print(f"Coop Members: {len(Coop_Members)}")
print("   " + "\n   ".join(Coop_Members))
print("---------------------------------------------")
print("\n")
# Print results