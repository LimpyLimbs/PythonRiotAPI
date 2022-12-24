import requests


class Summoner:
    def __init__(self, id, account_id, puuid, name, summoner_level):
        self.id = id
        self.account_id = account_id
        self.puuid = puuid
        self.name = name
        self.summoner_level = summoner_level

    def get_match_history(self):
        response = requests.get(f"https://na1.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids",
                                headers={"X-Riot-Token": "RGAPI-f1ffcb00-eb37-43f1-9697-15ea98c2e319"})
        print(self.puuid)
