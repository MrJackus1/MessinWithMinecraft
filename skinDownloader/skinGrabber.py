import requests
import json

def get_minecraft_skin(uuid):
    url = f"https://crafatar.com/skins/{uuid}"
    response = requests.get(url)

    if response.status_code == 200:
        with open("skin.png", "wb") as f:
            f.write(response.content)
        print(f"Skin for {uuid} saved as skin.png")
    else:
        print(f"Could not fetch skin for {uuid}. Error code: {response.status_code}")
        
def user2uuid(username):
    url = f"https://playerdb.co/api/player/minecraft/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        #print('200')
        x = json.loads(response.content)
        #print(x)
        print(x['data']["player"]["raw_id"])
        a = x['data']["player"]["raw_id"]
        return a
    else:
        print('Cannot resolve uuid...',response.status_code)

if __name__ == "__main__":
    username = input("Enter Minecraft username: ")
    #get_minecraft_skin(username)
    
    get_minecraft_skin(user2uuid(username))