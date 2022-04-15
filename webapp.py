# Author: Lucas Angelozzi
# Date: 04/11/22
# Purpose: practice application for final exam

# Imports
from flask import Flask, jsonify, request, render_template
from models.player import Player
from models.team import Team
from models.tournament import Tournament

# Creating a flask object
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home_page_player_info():
    """Renders html home page that displays the teams information

    Returns:
        template: the html page
    """
    
    provs = Tournament(Team("Ducks"), Team("Focus"))
    ducks = provs.get_team("Ducks")
    focus = provs.get_team("Focus")
    
    return render_template("home.html", ducks=ducks, focus=focus)

@app.route("/api/players", methods=["GET"])
def get_players():
    """Gets all of the players from all teams and returns them as json objects

    Returns:
        json: the players in the tournament
    """
    
    provs = Tournament(Team("Ducks"), Team("Focus"))
    data = list()

    for team in provs.teams:
        for player in team.players:
            data.append(player.to_dict())

    return jsonify(data), 200

@app.route("/api/players/<string:teamname>/<string:player_position>", methods=["GET"])
def get_players_by_pos(teamname, player_position):
    """Returns a list of JSON objects of all players on the team with the indicated position

    Args:
        teamname (str): the name of the team you want
        player_position (str): the position you want

    Returns:
        json: objects for all players on the team who have that position
    """
    
    provs = Tournament(Team("Ducks"), Team("Focus"))
    team = provs.get_team(teamname)
    
    players = team.get_players_by_position(player_position)
    data = [player.to_dict() for player in players]

    return jsonify(data), 200

@app.route("/api/players/<string:teamname>/edit/<string:player_name>", methods=["POST"])
def edit_position(teamname, player_name):
    """Edit a players position

    Args:
        teamname (str): the team the player is on
        player_name (str): the players full name

    Returns:
        json: the updated player information as a json object
    """
    
    provs = Tournament(Team("Ducks"), Team("Focus"))
    team = provs.get_team(teamname)
    body = request.json
    new_position = body["Position"]

    updated_player = team.edit_player_position(player_name, new_position)
    provs.save_info()
    if updated_player:
        return jsonify(updated_player.to_dict()), 201
    else:
        return jsonify({"Error": "Player not found"}), 404


@app.route("/api/players/<string:teamname>/add", methods=["POST"])
def add_player(teamname):
    """Add a player to a team

    Args:
        teamname (str): the team you want to add the player to

    Returns:
        json: the newly added player information as a json object
    """
    
    provs = Tournament(Team("Ducks"), Team("Focus"))
    team = provs.get_team(teamname)
    body = request.json

    added_player = team.add_player(body["Name"], body["Position"])
    provs.save_info()
    if added_player:
        return jsonify(added_player.to_dict()), 201
    else:
        return jsonify({"Error: Player info invalid"}), 400

@app.route("/api/players/<string:teamname>/delete/<string:player_name>", methods=["DELETE"])
def delete_player(teamname, player_name):
    """Remove a player from a team

    Args:
        teamname (str): the team the player is on
        player_name (str): the full name of the player you want to remove

    Returns:
        json: status message
    """
    
    provs = Tournament(Team("Ducks"), Team("Focus"))
    team = provs.get_team(teamname)
    
    deleted = team.remove_player(player_name)
    provs.save_info()
    if deleted:
        return jsonify({"Success": f"{player_name} has been successfully removed from the team"}), 200
    else:
        return jsonify({"Error": "Player not found"}), 404

if __name__ == "__main__":
    # Running the app in debug mode for develpment
    app.run(debug=True)