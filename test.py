# Riot API를 요청할 때 쓰는 HTTP 요청 도구
import requests

# URL에 들어가는 사용자 입력값을 안전하게 인코딩해주는 함수 (공백 등 처리)
from urllib.parse import quote

# ▶️ Riot 개발자 포털에서 받은 API 키 (꼭 유효한 키로 넣어야 함)
API_KEY = "RGAPI-e4ecb0e2-978b-4498-a0be-36f90d243729"

# ▶️ 유저의 닉네임 (Riot ID에서 '게임 이름' 부분)
game_name = "Hide on bush"

# ▶️ 유저의 태그라인 (ex: KR1, NA1, EUW 등 — Riot 계정에서 닉네임 뒤에 붙는 태그)
tag_line = "KR1"

# ▶️ Riot API의 Riot ID 요청 URL
#    이 URL에 game_name과 tag_line을 넣어서 실제로 조회함
url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

# ▶️ Riot API에 인증을 위한 헤더 정의
headers = {
    "X-Riot-Token": API_KEY,         # Riot이 발급한 API 키를 헤더에 넣어야 인증됨
    "User-Agent": "Mozilla/5.0"      # 일부 API는 User-Agent 없으면 막히기도 해서 관례적으로 넣어줌
}

# ▶️ 실제로 Riot 서버에 요청을 보냄 (GET 방식)
res = requests.get(url, headers=headers)

# ▶️ 응답을 JSON 형식으로 출력 (puuid, gameName, taSgLine 등이 들어 있음)
print(res.json())
