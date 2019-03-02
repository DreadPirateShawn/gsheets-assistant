import unittest

from gsheets_assistant.cell import Cell
from gsheets_assistant.utils import get_range, grid_range

class TestUtils(unittest.TestCase):

    def test_get_range(self):
        self.assertEqual('A1:A1', get_range(Cell.at('A1'), cols=1))
        self.assertEqual('A1:B1', get_range(Cell.at('A1'), cols=2))
        self.assertEqual('A1:A2', get_range(Cell.at('A1'), rows=2))
        self.assertEqual('A1:B2', get_range(Cell.at('A1'), cols=2, rows=2))
        self.assertEqual('B2:AC3', get_range(Cell.at('B2'), cols=28, rows=2))

        self.assertEqual('A1:A1', get_range(Cell.at('A1'), cols=1))
        self.assertEqual('A1:B1', get_range(Cell.at('A1'), cols=2))
        self.assertEqual('A1:A2', get_range(Cell.at('A1'), rows=2))
        self.assertEqual('A1:B2', get_range(Cell.at('A1'), cols=2, rows=2))
        self.assertEqual('B2:AC3', get_range(Cell.at('B2'), cols=28, rows=2))

        self.assertEqual('B2:B', get_range(Cell.at('B2'), cols=1, rows=-1))
        self.assertEqual('B2', get_range(Cell.at('B2'), cols=-1, rows=-1))

        self.assertEqual('C:D', get_range(Cell.at('C'), cols=2, rows=-1))
        self.assertEqual('3:4', get_range(Cell.at('3'), cols=-1, rows=2))

    def test_grid_range(self):
        self.assertEqual(grid_range('foo'), {
            'sheetId': 'foo',
        })

        self.assertEqual(grid_range('foo', 'A'), {
            'sheetId': 'foo',
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        })

        self.assertEqual(grid_range('foo', '1'), {
            'sheetId': 'foo',
            'startRowIndex': 0,
            'endRowIndex': 1,
        })

        self.assertEqual(grid_range('foo', 'B:C'), {
            'sheetId': 'foo',
            'startColumnIndex': 1,
            'endColumnIndex': 3,
        })

        self.assertEqual(grid_range('foo', 'A5:B'), {
            'sheetId': 'foo',
            'startColumnIndex': 0,
            'endColumnIndex': 2,
            'startRowIndex': 4,
        })

        self.assertEqual(grid_range('foo', 'A5'), {
            'sheetId': 'foo',
            'startColumnIndex': 0,
            'endColumnIndex': 1,
            'startRowIndex': 4,
            'endRowIndex': 5,
        })

        self.assertEqual(grid_range('foo', 'A1:A1'), {
            'sheetId': 'foo',
            'startColumnIndex': 0,
            'endColumnIndex': 1,
            'startRowIndex': 0,
            'endRowIndex': 1,
        })

        self.assertEqual(grid_range('foo', 'A3:B4'), {
            'sheetId': 'foo',
            'startColumnIndex': 0,
            'endColumnIndex': 2,
            'startRowIndex': 2,
            'endRowIndex': 4,
        })

