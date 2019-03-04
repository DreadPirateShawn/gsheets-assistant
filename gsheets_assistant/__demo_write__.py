import argparse
import httplib2

from gsheets_assistant.credentials import Credentials
from gsheets_assistant.spreadsheet import Spreadsheet
from gsheets_assistant.pages.data import demo_data
from gsheets_assistant.pages.formatting import demo_formatting
from gsheets_assistant.pages.movement import demo_movement
from gsheets_assistant.pages.formula import demo_formula

def main(secret_file=None, spreadsheet=None):
    # -- Get the relevant doc -- #
    creds = Credentials(secret_file).get()
    http = creds.authorize(httplib2.Http())
    sheet = Spreadsheet(http, spreadsheet)
    demo_data(sheet)
    demo_formatting(sheet)
    demo_movement(sheet)
    demo_formula(sheet)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--spreadsheet', type=str, help='Spreadsheet ID', required=True)
    parser.add_argument('--secret-file', type=str, help='Path to secret file', required=True)
    args = parser.parse_args()
    main(**vars(args))
