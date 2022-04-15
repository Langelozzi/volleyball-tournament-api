# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: practice application for final exam

# Imports
import json
from models.player import Player

class Team:
    def __init__(self, teamname: str) -> None:
        """Constructor method

        Args:
            teamname (str): the name of the team
        """
        
        self.teamname = teamname

        with open("data/players.json") as file:
            data = json.load(file)

            # Populating the players list with Player objects made from the JSON data
            # Only takes players whose teamname matches that of self.teamname
            self.players = [
                Player(player["Name"], player["Position"], player["Team"])
                for player in data
                if player["Team"].lower() == self.teamname.lower()
            ]
    
    def __str__(self) -> str:
        """Formats the string output of the object to be simmply the teamname

        Returns:
            str: the teamname string
        """

        return self.teamname

    def __len__(self) -> int:
        """Allows the object length to be seen as the amount of players on the team

        Returns:
            int: the number of players on the team
        """
        
        return len(self.players)

    def get_player_by_name(self, name: str) -> Player:
        """Gets a single player by name

        Args:
            name (str): the name of the player queried

        Returns:
            Player: the player object queried
        """

        for player in self.players:
            if player.name == name.lower():
                return player

    def get_players_by_position(self, position: str) -> list:
        """Gets all players that play the same position

        Args:
            position (str): the position requested

        Returns:
            list: all players who play that position
        """

        players = [
            player for player in self.players
            if player.position == position
        ]

        return players

    def edit_player_position(self, name: str, new_position: str) -> Player:
        """Changes the position attribute of the player name passed in

        Args:
            name (str): the name of the player you want to edit
            new_position (str): the position you want to change it to

        Returns:
            Player: the updated player object
        """
        
        player = self.get_player_by_name(name)
        try:
            player.position = new_position.lower()
            return player
        except:
            return None

    def add_player(self, name: str, position: str) -> Player:
        """Add a new player to the team

        Args:
            name (str): the name of the new player
            position (str): the position of the new player

        Returns:
            Player: if the player was added successfully or not
        """
        
        try:
            new_player = Player(name, position, self.teamname)
            self.players.append(new_player)
            return new_player
        except ValueError:
            return None

    def remove_player(self, name: str) -> bool:
        """removes a player from the self.players list

        Args:
            name (str): the name of the player you'd like to remove

        Returns:
            bool: whether or not the player was successfully removed
        """
        
        player = self.get_player_by_name(name)
        
        try:
            self.players.remove(player)
            return True
        except ValueError:
            return False



    