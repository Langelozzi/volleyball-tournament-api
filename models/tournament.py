# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: practice application for final exam

# Imports
import json
from models.team import Team

class Tournament:
    def __init__(self, *args) -> None:
        self.teams = [team for team in args] 
        
    def get_team(self, teamname: str) -> Team:
        for team in self.teams:
            if team.teamname == teamname:
                return team

    def save_info(self):
        players = list()
        for team in self.teams:
            for player in team.players:
                players.append(player.to_dict())

        with open("data/players.json", "w") as file:
            json.dump(players, file)

        

