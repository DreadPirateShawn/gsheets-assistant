from gsheets_assistant.cell import Cell
from gsheets_assistant.utils import get_range

def demo_movement(sheet):
    tab_name = "Gsheets Demo: Movement"

    # Delete/recreate the tab
    sheet.delete_tabs([tab_name])
    sheet.add_tabs([tab_name], rows=7, cols=7)

    # Get tab object
    tab = sheet.get_tab(tab_name)

    # Get cell pointers
    pointerA = Cell.at('A1')
    pointerB = pointerA.get_relative_cell(cols=6)
    pointerC = pointerA.get_relative_cell(rows=6)
    pointerD = pointerA.get_relative_cell(cols=6, rows=6)

    with tab.action_set():
        # Actions that can be safely performed together

        tab.formatting(pointerA, bg_color="#DDDDDD")
        tab.formatting(pointerB, bg_color="#DDDDDD")
        tab.formatting(pointerC, bg_color="#DDDDDD")
        tab.formatting(pointerD, bg_color="#DDDDDD")

        pointerA.move(rows=1, cols=1)
        pointerB.move(rows=1, cols=-1)
        pointerC.move(rows=-1, cols=1)
        pointerD.move(rows=-1, cols=-1)

        tab.formatting(pointerA, bg_color="#AAAAAA")
        tab.formatting(pointerB, bg_color="#AAAAAA")
        tab.formatting(pointerC, bg_color="#AAAAAA")
        tab.formatting(pointerD, bg_color="#AAAAAA")

        pointerA.move(rows=1, cols=1)
        pointerB.move(rows=1, cols=-1)
        pointerC.move(rows=-1, cols=1)
        pointerD.move(rows=-1, cols=-1)

        tab.formatting(pointerA, bg_color="#666666")
        tab.formatting(pointerB, bg_color="#666666")
        tab.formatting(pointerC, bg_color="#666666")
        tab.formatting(pointerD, bg_color="#666666")

        pointerA.move(rows=1, cols=1)
        tab.formatting(pointerA, bg_color="#000000")
