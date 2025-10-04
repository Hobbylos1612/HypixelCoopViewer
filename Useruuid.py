import requests
uuid = False
trys = 3
while not trys == 0:
    username = input("Enter Username ")
    Uuid_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    Uuid_response = requests.get(Uuid_url)
    if str(Uuid_response) == "<Response [404]>":
        print("Invalid Username")
        trys -= 1
    else:
        uuid = Uuid_response.json()["id"]
        print(uuid)