import requests
import summoner

response_code = 404
api_key = {"X-Riot-Token": "RGAPI-f1ffcb00-eb37-43f1-9697-15ea98c2e319"}

# checks for valid summoner name
while response_code != 200:
    summoner_name = input("Enter Summoner Name: ")
    response = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}',
                            headers=api_key)

    response_code = response.status_code

    if response_code != 200:
        print('Summoner name not found. Please try again.')

# formats api data to json
summoner_data = response.json()

summoner_object = summoner.Summoner(summoner_data["id"], summoner_data["accountId"], summoner_data["puuid"], summoner_data["name"], summoner_data["summonerLevel"])

print(summoner_object.summoner_level)
print(summoner_object.get_match_history())

