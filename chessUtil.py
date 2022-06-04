import requests
from chessApi import *
chess_url = "https://api.chess.com/"
exemple_id_match = "1155655"


def getBoardResultsFromPlayer(match, n_team, player):
    players = match['teams'][f'team{n_team}']['players']
    for player_c in players:
        if player_c['username'] == player:
            board = getBoardfromLink(player_c['board'])
            return board['board_scores'][player]


def getTeamNameFromMatch(match, n_team):
    return match['teams'][f'team{n_team}']['name']


def getPlayersUsernamesFromTeam(team):
    return [player['username'] for player in team['players']]


def getPlayersFromMatch(match):
    players = {}
    players[getTeamNameFromMatch(match, 1)] = getPlayersUsernamesFromTeam(match['teams']['team1'])
    players[getTeamNameFromMatch(match, 2)] = getPlayersUsernamesFromTeam(match['teams']['team2'])
    return players


def getResultsFromMatch(match):
    return [match['teams']['team1']['score'], match['teams']['team2']['score']]


def testing():
    match = getMatch(exemple_id_match)
    print(match)
    print(getResultsFromMatch(match))
    print(getTeamNameFromMatch(match, 1))
    print(getPlayersFromMatch(match))
    print(getBoardResultsFromPlayer(match, 1, "f645"))


def main():
    testing()
    pass


if __name__ == '__main__':
    main()