# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: practice application for final exam

'''File containing Tournament class'''

# Imports
import json
from models.team import Team

class Tournament:
    def __init__(self, *args) -> None:
        """Constructor method that creates list of all the teams.
        Number of teams is not limited because of *args.
        """
        
        self.teams = [team for team in args] 
        
    def get_team(self, teamname: str) -> Team:
        """Get a team object out of the tournament

        Args:
            teamname (str): the teamname

        Returns:
            Team: the Team object that you requested
        """
        
        for team in self.teams:
            if team.teamname == teamname:
                return team

    def save_info(self):
        """Writes any changes to the data/players.json file.
        """
        
        players = list()
        for team in self.teams:
            for player in team.players:
                players.append(player.to_dict())

        with open("data/players.json", "w") as file:
            json.dump(players, file)

        

