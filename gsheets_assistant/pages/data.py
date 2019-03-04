from gsheets_assistant.cell import Cell

def demo_data(sheet):
    tab_name = "Gsheets Demo: Data"

    # Delete/recreate the tab
    sheet.delete_tabs([tab_name])
    sheet.add_tabs([tab_name], rows=6, cols=6)

    # Get tab object
    tab = sheet.get_tab(tab_name)

    # Get cell pointer
    pointer = Cell.at('A1')

    with tab.action_set():
        # Actions that can be safely performed together

        # Write a single row of data
        tab.write_row(pointer, ['do','re','mi'])

        # Move down two rows
        pointer.move(rows=2)

        # Write data as list of row arrays
        tab.write_rows(pointer, [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
        ])

        # Move over 4 cols
        pointer.move(cols=4)

        # Write a single column of data
        tab.write_column(pointer, ['fa','so','la'])
