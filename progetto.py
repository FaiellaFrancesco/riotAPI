api_key="RGAPI-ed032c58-4e6c-4d77-84d8-4bde4de95b36"
api_game_info="https://europe.api.riotgames.com/lol/match/v5/matches/"


import requests
api_url="https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Schwarz/NERD?api_key=RGAPI-ed032c58-4e6c-4d77-84d8-4bde4de95b36"

api_url+'?api_key='+ api_key

api_match="https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/KNIBbobjBGxYT8PhB_sXWzOSRFrBOV5LQgZ4kQvuWh3i2vJ9-qke99IG-eVUU4PWbDYYhV8iWt1FUw/ids?start=0&count=20&api_key=RGAPI-ed032c58-4e6c-4d77-84d8-4bde4de95b36"
match_info=requests.get(api_url)
#print(match_info.json())

matches=requests.get(api_match).json()
match=matches[0]
#print(match)

api_game_info=api_game_info+match+'?api_key='+api_key

game_resp=requests.get(api_game_info).json()

durata=game_resp.get("info").get("gameDuration")
gameId=game_resp.get("info").get("gameId")
game_resp.keys()
suarz=None
#print(game_resp["info"]["participants"][1])

game_mod=game_resp.get("info").get("gameType")

for participants in game_resp["info"]["participants"]:
    
    if(participants.get("summonerName")=='Schwarz03'):
        suarz=participants
        #print(suarz)
        print("ULTIMO GAME DELLO SUARZ")
        
        champ=suarz.get("championName")
        kills=suarz.get("kills")
        deaths=suarz.get("deaths")
        assist=suarz.get("assists")
        minions=suarz.get("totalMinionsKilled")
        win=suarz.get("win")
        if(win==False):
            print("PERSO")
        else: print("VINTO")
        print(game_mod)
        print(f"Champion: {champ}")
        print(f"KDA: {kills} / {deaths} / {assist}")
        print(f"cs: {minions}")
        break   


