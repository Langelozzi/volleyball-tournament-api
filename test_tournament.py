# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: testing my player file

# Imports
import pytest
from unittest.mock import patch, mock_open
from models.team import Team
from models.tournament import Tournament

dummy_data = '''[
    {
        "Name": "Dana Liu",
        "Position": "Middle",
        "Team": "Ducks"
    },
    {
        "Name": "Trace Stewart",
        "Position": "Libero",
        "Team": "Ducks"
    },
    {
        "Name": "Elle Medina",
        "Position": "Setter",
        "Team": "Focus"
    },
    {
        "Name": "Maeve Clarke",
        "Position": "Right Side",
        "Team": "Focus"
    },
    {
        "Name": "Issac Howell",
        "Position": "Left Side",
        "Team": "Focus"
    },
    {
        "Name": "Halle Welch",
        "Position": "Left Side",
        "Team": "Focus"
    },
    {
        "Name": "Clark Mcdonald",
        "Position": "Middle",
        "Team": "Focus"
    }
]
'''

@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=dummy_data)
def focus(mock_file):
    team = Team("Focus")
    return team

@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=dummy_data)
def ducks(mock_file):
    team = Team("Ducks")
    return team

@pytest.fixture
def tournament(ducks, focus):
    return Tournament(ducks, focus)

def test_init(tournament):
    assert len(tournament.teams) == 2

def test_get_team(tournament):
    focus = tournament.get_team("Focus")
    assert str(focus) == "Focus"
    assert len(focus) == 5

def test_save(tournament):
    ducks = tournament.get_team("Ducks")
    ducks.add_player("John", "Middle")
    
    with patch('json.dump') as mock_json:
        with patch('builtins.open') as mock_file:
            tournament.save_info()
            assert mock_json.call_count == 1
            data = mock_json.call_args[0][0]

            assert mock_file.call_count == 1
            assert mock_file.call_args[0][0] == "data/players.json"
            assert mock_file.call_args[0][1] == "w"