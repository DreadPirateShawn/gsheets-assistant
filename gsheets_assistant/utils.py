from gsheets_assistant.cell import Cell, col_to_letters, letters_to_col


def get_range(cell, cols=1, rows=1):
    if isinstance(cell, str):
        cell = Cell.at(cell)

    col = cell.col
    row = cell.row

    if col and not isinstance(col, int):
        col = letters_to_col(col)

    # Start of range

    start = col_to_letters(col)

    if row:
        start += str(row)

    # End of range

    if cols < 0:
        end_col = ''
    else:
        end_col = col_to_letters(col + cols - 1)

    if rows < 0:
        end_row = ''
    else:
        end_row = str(row + rows - 1)

    end = end_col + end_row

    # Range

    verdict = start
    if end:
        verdict += ':' + end

    return verdict


def grid_range(tab_id, range_name=None):
    """ https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets#GridRange """

    if isinstance(range_name, Cell):
        range_name = str(range_name)

    data = {
        'sheetId': tab_id,
    }

    if not range_name:
        pass

    elif range_name.isdigit():
        data['startRowIndex'] = int(range_name) - 1
        data['endRowIndex'] = int(range_name)

    elif ':' not in range_name:
        cell = Cell.at(range_name)

        if cell.col:
            data['startColumnIndex'] = cell.col - 1
            data['endColumnIndex'] = cell.col

        if cell.row:
            data['startRowIndex'] = cell.row - 1
            data['endRowIndex'] = cell.row

    else:
        start, end = range_name.split(':')

        start_cell = Cell.at(start)

        if start_cell.col:
            data['startColumnIndex'] = start_cell.col - 1

        if start_cell.row:
            data['startRowIndex'] = start_cell.row - 1

        end_cell = Cell.at(end)

        if end_cell.col:
            data['endColumnIndex'] = end_cell.col

        if end_cell.row:
            data['endRowIndex'] = end_cell.row

    return data


def hex_to_rgb_hash(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    if not value:
        value = "#EFEFEF"

    value = value.lstrip('#')

    if len(value) != 6:
        raise Exception("hex_to_rgb_hash expects hex color of length, eg #FF0000, but got %s" % value)

    round(int('EF', 16) / 255.0, 2)

    return {
        'red': round(int(value[:2], 16) / 255.0, 1),
        'green': round(int(value[2:4], 16) / 255.0, 1),
        'blue': round(int(value[4:], 16) / 255.0, 1),
    }

