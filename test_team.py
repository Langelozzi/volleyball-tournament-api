# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: testing my team file

# Imports
import pytest
from unittest.mock import patch, mock_open
from models.team import Team

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

def test_init(focus):
    assert focus.teamname == "Focus"
    assert len(focus.players) == 5

def test_str(focus):
    assert str(focus) == "Focus"

def test_len(focus):
    assert len(focus) == 5

def test_get_by_position(focus):
    powers = focus.get_players_by_position("left side")

    assert len(powers) == 2
    assert "halle welch" in [p.name for p in powers]

def test_change_position(focus):
    for p in focus.players:
        if p.name == "clark mcdonald":
            player = p

    assert player.name == "clark mcdonald"
    assert player.position == "middle"

    updated_player = focus.edit_player_position("clark mcdonald", "setter")

    assert updated_player.name == "clark mcdonald"
    assert updated_player.position == "setter"

def test_add_player(focus):
    added = focus.add_player("Lucas", "libero")
    assert "lucas" in [player.name for player in focus.players]
    assert added == True

def test_bad_add(focus):
    added = focus.add_player("lucas", "catcher")
    assert added == False
    assert "lucas" not in [player.name for player in focus.players]

def test_remove(focus):
    removed = focus.remove_player("halle welch")
    assert removed == True
    assert "halle welch" not in [player.name for player in focus.players]

def test_bad_remove(focus):
    removed = focus.remove_player("brett welch")
    assert removed == False