import gspread
from oauth2client.service_account import ServiceAccountCredentials
import constants
import time



def connect():
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('sinuous-analog-342722-04666296f155.json', scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)
    return client


def getPaxesList(client, nameFiles):
    dict = {}
    for name in nameFiles:
        dict[name] = getPaxList(client, name)
        time.sleep(3)
    return dict


def getPaxList(client, nameFile):
    sheet = opensheet(client, nameFile)
    sheet_inst = sheet.get_worksheet(0)
    rows = sheet_inst.get_all_records(head=2)
    return [player['Nickname Chess'] for player in rows]


def opensheet(client, nameFile):
    try:
        sheet = client.open(nameFile)
    except gspread.SpreadsheetNotFound as err:
        print(err)
        return
    return sheet


def main():
    pass


if __name__ == "__main__":
    main()