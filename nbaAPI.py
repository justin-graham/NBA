from nba_api.stats.static import teams
from nba_api.stats.static import players
import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import playergamelog


teams = teams.get_teams()
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_ID = GSW['id']
GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable = GSW_ID).get_data_frames()[0]

players_dict = players.get_players()
lebron = [player for player in player_dict if player['full_name'] == 'Lebron James'][0]
lebron_id = lebron['id']
game_log = playergamelog.PlayerGameLog(player = lebron_id, season = '2024').get_data_frames()
