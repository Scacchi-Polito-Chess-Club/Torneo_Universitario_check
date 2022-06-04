import requests
chess_url = "https://api.chess.com/"


def getMatch(match_id):
    r = requests.get(chess_url + f"pub/match/live/{match_id}")
    if r: return r.json()


def getBoardfromLink(board_link):
    r = requests.get(board_link)
    if r: return r.json()