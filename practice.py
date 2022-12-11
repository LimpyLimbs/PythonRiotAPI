import requests

response_code = 404

while response_code != 200:
    summoner_name = input("Enter Summoner Name: ")
    response = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}',
                            headers={"X-Riot-Token": "RGAPI-1fb5f97f-7355-4d46-b7e0-779ec346093b"})
    response_code = response.status_code

    if response_code != 200:
        print('Summoner name not found. Please try again.')

print(response.json())




'''
To Do:

While loop for checking whether response is 200ok
Function for editing summoner name in the HTTPS URL
'''

