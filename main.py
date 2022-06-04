import sys
import chessApi
import chessUtil
import driveApi
from termcolor import colored


def menu():
    print("Menu:")
    print("1 - Definisci gli ID dei match")
    print("2 - Controlla i partecipanti dei match definiti")
    print("3 - Stampa tutti i risultati(raw)")
    print("\n0 - Esci")
    i = int(input("\n> "))
    return i


def defineMatchIds():
    nmatch = int(input("Quanti match vuoi controllare? "))
    match_ids = []
    for i in range(nmatch): match_ids.append(input(f"Inserire ID numero {i+1}: "))
    print("Inserimento completo!")
    return match_ids


def printResults(match_ids):
    print("Printing results:")
    for id in match_ids:
        match = chessApi.getMatch(id)
        teams = [chessUtil.getTeamNameFromMatch(match, 1), chessUtil.getTeamNameFromMatch(match, 2)]
        scores = chessUtil.getResultsFromMatch(match)
        print(f"\n{teams[0]} {scores[0]} - {teams[1]} {scores[1]}")


def checkPlayers(match_ids):
    client = driveApi.connect()
    for match_id in match_ids:
        match = chessApi.getMatch(match_id)
        team1 = chessUtil.getTeamNameFromMatch(match, 1)
        team2 = chessUtil.getTeamNameFromMatch(match, 2)
        scores = chessUtil.getResultsFromMatch(match)
        partecipants1 = driveApi.getPartecipants(client, team1)
        partecipants2 = driveApi.getPartecipants(client, team2)
        players = chessUtil.getPlayersFromMatch(match)
        print(f"Chechink match {match_id}: {team1} {scores[0]} VS {scores[1]} {team2}")
        malus_tot = [0.0, 0.0]
        for player in players[team1]:
            if player.lower() not in [partecipant.lower() for partecipant in partecipants1]:
                print(colored(f"Il giocatore {player} non è in lista di {team1}", "red"))
                malus = chessUtil.getBoardResultsFromPlayer(match, 1, player)
                print(colored(f"Verranno sottratti: {malus} punti\n", "red"))
                malus_tot[0] += malus
        for player in players[team2]:
            if player.lower() not in [partecipant.lower() for partecipant in partecipants2]:
                print(colored(f"Il giocatore {player} non è in lista di {team2}", "red"))
                malus = chessUtil.getBoardResultsFromPlayer(match, 2, player)
                print(colored(f"Verranno sottratti: {malus} punti\n", "red"))
                malus_tot[1] += malus
        if malus_tot[0] + malus_tot[1] > 0 : print(f"\nNuovi risultati : {team1} {scores[0]-malus_tot[0]} VS {scores[1]-malus_tot[0]} {team2}")


def main():
    i = menu()
    match_ids = ""
    while(i!=0):
        if i == 1:
            match_ids = defineMatchIds()
        elif i == 2:
            if match_ids == "": sys.exit("Devi prima definire gli ID!")
            checkPlayers(match_ids)
        elif i == 3:
            printResults(match_ids)
        i = menu()
    return


if __name__ == "__main__":
    main()