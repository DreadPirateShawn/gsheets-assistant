import argparse
import httplib2

from gsheets_assistant.credentials import Credentials
from gsheets_assistant.spreadsheet import Spreadsheet
from gsheets_assistant.utils import get_range

# Per https://developers.google.com/sheets/api/quickstart/apps-script and similar
DEMO_SPREADSHEET = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"

def main(secret_file=None):
    creds = Credentials(secret_file).get()
    http = creds.authorize(httplib2.Http())
    sheet = Spreadsheet(http, DEMO_SPREADSHEET)
    tab = sheet.get_tab('Class Data')
    values = tab.read('A1:E')

    if not values:
        print('No data found.')
    else:
        print('== Sample data found: ==')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--secret-file', type=str, help='Path to secret file', required=True)
    args = parser.parse_args()
    main(**vars(args))
