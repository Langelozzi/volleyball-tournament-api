# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: unit testing my player file

# Imports
import pytest
from models.player import Player

# Fixture allows me to reuse my lucas player object in multiple tests
@pytest.fixture
def lucas():
    '''represents a regular valid player'''
    player = Player("Lucas Angelozzi", "Libero", "Ducks")

    return player

def test_invalid_arg_types():
    '''Testing argument types other than strings for each argument'''
    with pytest.raises(ValueError):
        player = Player(123, "libero", "ducks") 
    
    with pytest.raises(ValueError):
        player = Player("Lucas", {"position": "middle"}, "ducks") 
    
    with pytest.raises(ValueError):
        player = Player("Lucas", "libero", 456) 

def test_invalid_position():
    '''Testing for an invalid position type'''
    with pytest.raises(ValueError):
        player = Player("Lucas", "power", "ducks")

def test_init(lucas):
    '''Testing that the player attributes are initilized in constructor'''
    assert lucas.name == "lucas angelozzi"
    assert lucas.position == "libero"
    assert lucas.team == "ducks"

def test_player_string(lucas):
    '''Checking that printing as a string returns the formated information'''
    string = str(lucas)
    assert "Name: lucas angelozzi" in string
    assert "Position: libero" in string
    assert "Team: ducks" in string

def test_to_dict(lucas):
    '''Testing the to_dict() function'''
    correct = {
        "Name": "lucas angelozzi",
        "Position": "libero",
        "Team": "ducks"
    }
    assert lucas.to_dict() == correct