import argparse
import httplib2
import os

from gsheets_assistant.credentials import Credentials
from gsheets_assistant.spreadsheet import Spreadsheet
from gsheets_assistant.cell import Cell
from gsheets_assistant.utils import col_to_letters, get_range
from gsheets_assistant.pages.sample import page_sample

def main(spreadsheet=None):
    # -- Get the relevant doc -- #
    creds = Credentials().get()
    http = creds.authorize(httplib2.Http())
    sheet = Spreadsheet(http, spreadsheet)

    # -- Spot-check functionality -- #
    tab = sheet.get_tab('Sheet1')
    values = tab.read('A1:B1')

    if not values:
        print('No data found.')
    else:
        print('== Sample data found: %r ==' % values)

    sheet.delete_tabs( sheet.list_all_but_first_tab() )
    sheet.add_tabs(["testing"], rows=50, cols=30)
    tab = sheet.get_tab("testing")
    page_sample(tab)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--spreadsheet', type=str, help='Spreadsheet ID', required=True)
    args = parser.parse_args()
    main(**vars(args))
