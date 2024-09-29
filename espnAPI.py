import requests
api_url = "https://cdn.nba.com/static/json/liveData/boxscore/boxscore_0022200056.json"
response = requests.get(api_url)
print(response.json())
