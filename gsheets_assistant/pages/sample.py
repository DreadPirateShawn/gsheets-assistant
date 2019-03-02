from gsheets_assistant.cell import Cell
from gsheets_assistant.utils import get_range


def page_sample(tab):
    header_cell = Cell.at('A1')
    subheader_cell = header_cell.get_relative_cell(rows=1)
    data_cell = header_cell.get_relative_cell(rows=2)

    with tab.action_set():
        # Format top header row
        tab.formatting("1", align_horiz="CENTER", bg_color="#AAAAAA", font_size=12, bold=True)
        tab.formatting("2", align_horiz="CENTER", bg_color="#CCCCCC", font_size=10, bold=True)
        tab.border(get_range(header_cell, cols=-1, rows=1), location='bottom', style='DASHED', width=1, color='#000000')
        tab.border(get_range(subheader_cell, cols=-1, rows=1), location='bottom', style='SOLID', width=2, color='#000000')

        tab.write_rows(data_cell, [
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i']
        ])
