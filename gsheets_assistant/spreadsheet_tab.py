from gsheets_assistant.api import Api
from gsheets_assistant.utils import get_range, grid_range, hex_to_rgb_hash

class SpreadsheetTab(Api):

    tab_name = None
    tab_id = None

    def __init__(self, http, spreadsheet_id, tab_name, tab_id):
        super(SpreadsheetTab, self).__init__(http, spreadsheet_id)
        self.tab_name = tab_name
        self.tab_id = tab_id


    def full_range_name(self, range_name):
        return self.tab_name + "!" + range_name


    # -- READING -- #

    def read(self, range_name):
        result = self.service.spreadsheets().values() \
                     .get(spreadsheetId=self.spreadsheet_id, range=self.full_range_name(range_name)) \
                     .execute()

        return result.get('values', [])


    # -- WRITING -- #

    def write_row(self, cell, values):
        self.write_rows(cell, [values])

    def write_rows(self, cell, values):
        if values and values[0]:
            self.add_values({
                'range': self.full_range_name(get_range(cell, cols=len(values[0]), rows=len(values))),
                'majorDimension': "ROWS",
                'values': values,
            })

    def write_column(self, cell, values):
        self.add_values({
            'range': self.full_range_name(get_range(cell, rows=len(values))),
            'majorDimension': "COLUMNS",
            'values': [values],
        })

    def write_formula(self, range_name, formula):
        self.add_action('repeatCell', {
            'range': grid_range(self.tab_id, range_name),
            'cell': {
                'userEnteredValue': {
                    'formulaValue': formula,
                }
            },
            'fields': "userEnteredValue",
        })


    # -- FORMATTING -- #

    def merge(self, range_name):
        self.add_action('mergeCells', {
            'mergeType': 'MERGE_ALL',
            'range': grid_range(self.tab_id, range_name),
        })


    def formatting(self, range_name, align_horiz=None, bg_color=None, fg_color=None, font_size=None, bold=False):
        format_data = {}
        text_format_data = {}

        if align_horiz:
            format_data['horizontalAlignment'] = align_horiz

        if bg_color:
            format_data['backgroundColor'] = hex_to_rgb_hash(bg_color)

        if fg_color:
            text_format_data['foregroundColor'] = hex_to_rgb_hash(fg_color)

        if font_size:
            text_format_data['fontSize'] = font_size

        if bold:
            text_format_data['bold'] = True

        if text_format_data:
            format_data['textFormat'] = text_format_data

        self.add_action('repeatCell', {
            'range': grid_range(self.tab_id, range_name),
            'cell': {
                'userEnteredFormat': format_data,
            },
            'fields': "userEnteredFormat(%s)" % ','.join(format_data.keys()),
        })


    def border(self, range_name, location, style, width, color):
        self.add_action('updateBorders', {
            'range': grid_range(self.tab_id, range_name),
            location: {
                'style': style,
                'width': width,
                'color': hex_to_rgb_hash(color),
            },
        })


    def auto_resize(self, column_range):
        raw_range = grid_range(self.tab_id, column_range)

        self.add_action('autoResizeDimensions', {
            "dimensions": {
                "sheetId": self.tab_id,
                "dimension": "COLUMNS",
                "startIndex": raw_range.get('startColumnIndex'),
                "endIndex": raw_range.get('endColumnIndex', raw_range.get('startColumnIndex') + 1),
            }
        })


    # -- RANGE PROTECTION -- #

    def protect_range(self, range_name, description):
        self.add_action('addProtectedRange', {
            'protectedRange': {
                'range': grid_range(self.tab_id, range_name),
                'description': description,
                'warningOnly': True,
            }
        })

