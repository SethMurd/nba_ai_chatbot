from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, leaguestandings, leaguegamefinder
import pandas as pd

def get_player_stats(player_name):
    """
    Fetches career stats for a given player name.
    """
    # Find player by name
    player_list = players.get_players()
    player = next((p for p in player_list if p["full_name"].lower() == player_name.lower()), None)

    if not player:
        return f"Error: Player '{player_name}' not found."

    # Fetch career stats using player ID
    player_id = player["id"]
    stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = stats.get_data_frames()[0]  # Convert to DataFrame

    return df.to_dict(orient="records")  # Convert DataFrame to a list of dictionaries

def get_team_standings():
    """
    Retrieves current NBA team standings.
    """
    standings = leaguestandings.LeagueStandings()
    df = standings.get_data_frames()[0]

    # Select relevant columns
    columns = ["TeamID", "TeamCity", "TeamName", "Conference", "WINS", "LOSSES", "WinPCT"]
    return df[columns].to_dict(orient="records")

def get_last_game(team_name):
    """
    Fetches the last game result for a given team.
    """
    team_list = teams.get_teams()
    team = next((t for t in team_list if t["full_name"].lower() == team_name.lower()), None)

    if not team:
        return f"Error: Team '{team_name}' not found."

    team_id = team["id"]

    # Get last game
    game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = game_finder.get_data_frames()[0]

    last_game = games.iloc[0]  # Get the most recent game

    # Calculate opponent's score
    opponent_points = last_game["PTS"] - last_game["PLUS_MINUS"]

    return {
        "team": team_name,
        "opponent": last_game["MATCHUP"],
        "date": last_game["GAME_DATE"],
        "score": f"{int(last_game['PTS'])} - {int(opponent_points)}",
        "win/loss": "Win" if last_game["WL"] == "W" else "Loss"
    }
def get_next_game(team_name):
    """
    Placeholder function for fetching the next scheduled game.
    Currently, nba_api does not provide future schedules.
    """
    return f"Upcoming game data for {team_name} is currently unavailable via nba_api."