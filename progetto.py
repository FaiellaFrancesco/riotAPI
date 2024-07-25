import requests

api_key = "RGAPI-0eb4650f-b5ba-4b67-a387-83ec4d374c81"
api_game_info = "https://europe.api.riotgames.com/lol/match/v5/matches/"

def get_puuid(summonerId=None, gameName=None, tagLine=None, region='europe'):
    api_account = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={api_key}"
    resp = requests.get(api_account)
    if resp.status_code == 200:
        return resp.json()["puuid"]
    else:
        print(f"Errore: {resp.status_code}")
        return None

def get_matches(puuid, start=0, count=50):
    api_matches = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={api_key}"
    resp = requests.get(api_matches)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Errore: {resp.status_code}")
        return None

def get_match_data_fromId(match_id=None,region='europe'):
    api_matches_data = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}/?api_key={api_key}"
    response=requests.get(api_matches_data)
    return response.json()


def stampaGame(participant):
    print("VINTO" if participant['win'] else "PERSO")
    print(participant['game_mod'])
    champ = participant['championName']
    kills = participant['kills']
    deaths = participant['deaths']
    assist = participant['assists']
    minions = participant['totalMinionsKilled']
    print(f"Champion: {champ}")
    print(f"KDA: {kills} / {deaths} / {assist}")
    print(f"CS: {minions}")

# Esempio di utilizzo delle funzioni
gameName = "Schwarz"
tagLine = "NERD"

puuid = get_puuid(gameName=gameName, tagLine=tagLine)

def suarz(aaa):
    if puuid:
        matches = get_matches(puuid)
        if matches:
            match = matches[0]
            api_game_info = api_game_info + match + '?api_key=' + api_key
            game_resp = requests.get(api_game_info).json()

            durata = game_resp.get("info").get("gameDuration")
            gameId = game_resp.get("info").get("gameId")
            suarz = None
            game_mod = game_resp.get("info").get("gameType")

            for participant in game_resp["info"]["participants"]:
                if participant.get("summonerName") == 'Schwarz03':
                    participant['game_mod'] = game_mod # qui devo aggiungerlo perforza, le informazioni sulla modalita sono sul game non sul partecipante
                    stampaGame(participant)
                    break


game=get_match_data_fromId('EUW1_7037688785')
metadata=game['metadata']
info=game['info']
players=info['participants']
match_Id=metadata['matchId']
teams=info['teams']

for player in players:
   

