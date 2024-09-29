from basketball_reference_web_scraper import client

client.players_advanced_season_totals(season_end_year=2024)

from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

client.players_advanced_season_totals(
    season_end_year=2024, 
    output_type=OutputType.JSON, 
    output_file_path="./2023_2024_advanced_player_season_totals.json"
)
