# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: practice application for final exam

'''File containing Player class'''

class Player:
    def __init__(self, name: str, position: str, team: str) -> None:
        """Constructor method

        Args:
            name (str): Player full name
            position (str): Player position
            team (str): Team in which player is a part of

        Raises:
            ValueError: if arguments are not strings
            ValueError: if the position is not a valid volleyball position
        """
        
        if type(name) is not str or type(position) is not str or type(team) is not str:
            raise ValueError
        if position.lower() not in ["setter", "left side", "right side", "middle", "libero"]:
            raise ValueError

        self.name = name.lower()
        self.position = position.lower()
        self.team = team.lower()

    def __str__(self) -> str:
        """Shows the player information nicely when object is printed

        Returns:
            str: the formatted player information
        """
        
        return f"Name: {self.name}\nPosition: {self.position}\nTeam: {self.team}"

    def to_dict(self) -> dict:
        """Converts the player object into a dictionary 

        Returns:
            dict: the dictionary with the player information
        """
        
        return {"Name": self.name, "Position": self.position, "Team": self.team}

        

