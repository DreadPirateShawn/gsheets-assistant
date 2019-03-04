from gsheets_assistant.cell import Cell
from gsheets_assistant.utils import get_range

def demo_formatting(sheet):
    tab_name = "Gsheets Demo: Formatting"

    # Delete/recreate the tab
    sheet.delete_tabs([tab_name])
    sheet.add_tabs([tab_name], rows=4, cols=3, color="#0000AA")

    # Get tab object
    tab = sheet.get_tab(tab_name)

    # Get cell pointers
    header_cell = Cell.at('A1')
    subheader_cell = header_cell.get_relative_cell(rows=1)
    data_cell = header_cell.get_relative_cell(rows=2)

    with tab.action_set():
        # Actions that can be safely performed together

        # Ranges, e.g. "A1:B10" or "A" (column) or "3" (row)
        header_range = get_range(header_cell, cols=-1, rows=1)
        subheader_range = get_range(subheader_cell, cols=-1, rows=1)

        # Format top header row
        tab.formatting(
            header_range,
            align_horiz="CENTER",
            bg_color="#AAAAAA",
            font_size=12,
            bold=True
        )
        tab.border(
            header_range,
            location='bottom',
            style='DASHED',
            width=1,
            color='#000000'
        )
        tab.formatting(
            subheader_range,
            align_horiz="CENTER",
            bg_color="#CCCCCC",
            font_size=10,
            bold=True
        )
        tab.border(
            subheader_range,
            location='bottom',
            style='SOLID',
            width=2,
            color='#000000'
        )

        # Write some data
        tab.write_row(header_cell, ['Header Row','Value #1'])
        tab.write_row(subheader_cell, ['Subheader Row','Value #2'])
        tab.write_row(data_cell, ['Data Row','Value #3'])

        # Auto-resize
        tab.auto_resize("A:C")

