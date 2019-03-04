import unittest

from gsheets_assistant.cell import Cell, col_to_letters, letters_to_col

class TestCell(unittest.TestCase):

    def test_cell(self):
        cell = Cell(col=1, row=2)
        self.assertEqual(1, cell.col)
        self.assertEqual(2, cell.row)

        self.assertEqual('A', cell.col_letter)

    def test_cell_at(self):
        cell = Cell.at('A2')
        self.assertEqual(1, cell.col)
        self.assertEqual(2, cell.row)

        self.assertEqual('A', cell.col_letter)

    def test_cell_at_column_only(self):
        cell = Cell.at('B')
        self.assertEqual(2, cell.col)
        self.assertEqual(None, cell.row)

        self.assertEqual('B', cell.col_letter)

    def test_cell_at_row_only(self):
        cell = Cell.at('2')
        self.assertEqual(None, cell.col)
        self.assertEqual(2, cell.row)

        self.assertEqual('', cell.col_letter)

    def test_string_representation(self):
        cell = Cell.at('A2')
        self.assertEqual('A2', str(cell))

        cell = Cell.at('B')
        self.assertEqual('B', str(cell))

        cell = Cell.at('3')
        self.assertEqual('3', str(cell))

    def test_move(self):
        cell = Cell.at('A2')
        self.assertEqual(1, cell.col)
        self.assertEqual(2, cell.row)

        cell.move(cols=3)
        self.assertEqual(4, cell.col)
        self.assertEqual(2, cell.row)

        cell.move(cols=-2)
        self.assertEqual(2, cell.col)
        self.assertEqual(2, cell.row)

        cell.move(rows=3)
        self.assertEqual(2, cell.col)
        self.assertEqual(5, cell.row)

        cell.move(rows=-2)
        self.assertEqual(2, cell.col)
        self.assertEqual(3, cell.row)

    def test_get_relative_cell(self):
        cell = Cell.at('A2')
        relative = cell.get_relative_cell(cols=3, rows=2)
        self.assertEqual(str(relative), 'D4')

        cell = Cell.at('B')
        relative = cell.get_relative_cell(cols=3, rows=2)
        self.assertEqual(str(relative), 'E')

        cell = Cell.at('3')
        relative = cell.get_relative_cell(cols=3, rows=2)
        self.assertEqual(str(relative), '5')

    def test_col_to_letter(self):
        self.assertEqual('A', col_to_letters(1))
        self.assertEqual('Z', col_to_letters(26))
        self.assertEqual('AA', col_to_letters(27))
        self.assertEqual('AZ', col_to_letters(52))
        self.assertEqual('AAA', col_to_letters(703))

    def test_letters_to_col(self):
        self.assertEqual(1, letters_to_col('A'))
        self.assertEqual(26, letters_to_col('Z'))
        self.assertEqual(27, letters_to_col('AA'))
        self.assertEqual(52, letters_to_col('AZ'))
        self.assertEqual(703, letters_to_col('AAA'))

