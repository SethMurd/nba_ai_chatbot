from fastapi import FastAPI
from app.nba_api_utils import get_player_stats, get_team_standings, get_last_game

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the NBA AI API"}

@app.get("/player/{player_name}")
def player_stats(player_name: str):
    return get_player_stats(player_name)

@app.get("/standings")
def standings():
    return get_team_standings()

@app.get("/last_game/{team_name}")
def last_game(team_name: str):
    return get_last_game(team_name)

