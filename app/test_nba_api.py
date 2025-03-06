from nba_api_utils import *

def test_nba_api():
    print("Fetching LeBron James' stats...")
    print(get_player_stats("LeBron James"))

    print("\nFetching NBA team standings...")
    print(get_team_standings())

    print("\nFetching last game result for Golden State Warriors...")
    print(get_last_game("Golden State Warriors"))

if __name__ == "__main__":
    test_nba_api()