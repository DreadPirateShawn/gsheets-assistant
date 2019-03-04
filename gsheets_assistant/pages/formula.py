from gsheets_assistant.cell import Cell
from gsheets_assistant.utils import get_range

def demo_formula(sheet):
    tab_name = "Gsheets Demo: Formula"

    # Delete/recreate the tab
    sheet.delete_tabs([tab_name])
    sheet.add_tabs([tab_name], rows=4, cols=5)

    # Get tab object
    tab = sheet.get_tab(tab_name)

    # Get cell pointers
    data_cell = Cell.at('A2')
    header_cell = Cell.at('D1')

    with tab.action_set():
        # Actions that can be safely performed together

        # Write basic headers
        tab.write_row(header_cell, ["Sum", "Average"])

        # Write some data
        tab.write_rows(data_cell, [
            [2, 3, 5],
            [7, 11, 13],
            [17, 19, 23],
        ])

        tab.write_formula(
            get_range(data_cell.get_relative_cell(cols=3)),
            "=SUM(%s)" % get_range(data_cell, cols=3)
        )
        tab.write_formula(
            get_range(data_cell.get_relative_cell(cols=4)),
            "=AVERAGE(%s)" % get_range(data_cell, cols=3)
        )

        data_cell.move(rows=1)

        tab.write_formula(
            get_range(data_cell.get_relative_cell(cols=3)),
            "=SUM(%s)" % get_range(data_cell, cols=3)
        )
        tab.write_formula(
            get_range(data_cell.get_relative_cell(cols=4)),
            "=AVERAGE(%s)" % get_range(data_cell, cols=3)
        )

        data_cell.move(rows=1)

        tab.write_formula(
            get_range(data_cell.get_relative_cell(cols=3)),
            "=SUM(%s)" % get_range(data_cell, cols=3)
        )
        tab.write_formula(
            get_range(data_cell.get_relative_cell(cols=4)),
            "=AVERAGE(%s)" % get_range(data_cell, cols=3)
        )

