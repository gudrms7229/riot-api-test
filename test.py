import requests
from urllib.parse import quote

API_KEY = "RGAPI-e4ecb0e2-978b-4498-a0be-36f90d243729"
game_name = "Hide on bush"
tag_line = "KR1"

url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
headers = {
    "X-Riot-Token": API_KEY,
    "User-Agent": "Mozilla/5.0"
    
}

res = requests.get(url, headers=headers)
print(res.json())
