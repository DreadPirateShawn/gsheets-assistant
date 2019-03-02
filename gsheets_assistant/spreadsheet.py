from gsheets_assistant.api import Api
from gsheets_assistant.spreadsheet_tab import SpreadsheetTab


class Spreadsheet(Api):

    tabs_lookup = None

    def __init__(self, http, spreadsheet_id):
        super(Spreadsheet, self).__init__(http, spreadsheet_id)
        self.check_tabs()


    def check_tabs(self):
        result = self.service.spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
        tabs = result.get('sheets', [])

        self.tabs_lookup = {}
        for tab in tabs:
            self.tabs_lookup[tab['properties']['title']] = tab['properties']


    def tab_id(self, tab_name):
        return self.tabs_lookup.get(tab_name, {}).get('sheetId', None)


    def list_all_but_first_tab(self):
        return [key for key,value in self.tabs_lookup.items() if value['sheetId']]


    def add_tabs(self, tab_names, rows=100, cols=50):
        for tab_name in tab_names:
            if tab_name in self.tabs_lookup:
                print "== WARNING: Tab '%s' already exists ==" % tab_name
                continue

            self.add_action('addSheet', {
                "properties": {
                    "title": tab_name,
                    "gridProperties": {
                        "rowCount": rows,
                        "columnCount": cols,
                    },
                    "tabColor": {
                        "red": 1.0,
                        "green": 0.3,
                        "blue": 0.4
                    }
                }
            })

        self.flush()
        self.check_tabs()


    def delete_tabs(self, tab_names):
        for tab_name in tab_names:
            if tab_name not in self.tabs_lookup:
                print "== WARNING: Tab '%s' does not exist ==" % tab_name
                continue

            self.add_action('deleteSheet', {
                "sheetId": self.tab_id(tab_name)
            })

        self.flush()
        self.check_tabs()


    def get_tab(self, tab_name):
        tab_id = self.tab_id(tab_name)

        # Note: tab_id can be 0 for initial tab, so compare to None explicitly.
        if tab_id == None:
            print "== WARNING: Tab '%s' does not exist ==" % tab_name
            return None

        return SpreadsheetTab(self.http, self.spreadsheet_id, tab_name, tab_id)

