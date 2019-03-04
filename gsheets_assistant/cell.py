import math
import re

CELL_PATTERN = re.compile(r'(?P<col>[A-Z]*)(?P<row>[0-9]*)')

def cell_components(cell_name):
    parts = CELL_PATTERN.match(cell_name)
    if parts:
        return parts.group('col'), parts.group('row')
    return None, None

def col_to_letters(col):
    letters = ''
    if not col:
        return letters
    while col > 0:
        mod = (col - 1) % 26
        letters = chr(ord('A') + mod) + letters
        col = (col - mod - 1) // 26
    return letters

def letters_to_col(letters):
    if isinstance(letters, int):
        return letters # not actually letters

    col = 0
    for idx,letter in enumerate(letters):
        col += (ord(letter) - ord('A') + 1) * int(math.pow(26, len(letters) - idx - 1))
    return col


class Cell(object):

    col = None
    row = None

    def __init__(self, col=None, row=None):
        if col:
            self.col = letters_to_col(col)
        if row:
            self.row = int(row)

    def __str__(self):
        display = ''
        if self.col:
            display += self.col_letter
        if self.row:
            display += str(self.row)
        return display

    def move(self, cols=0, rows=0):
        self.col += cols
        self.row += rows

    @classmethod
    def at(cls, label):
        col, row = cell_components(label)
        return Cell(col=col, row=row)

    def get_relative_cell(self, cols=0, rows=0):
        new_cols = new_rows = None
        if self.col:
            new_cols = self.col + cols
        if self.row:
            new_rows = self.row + rows
        return Cell(col=new_cols, row=new_rows)

    @property
    def col_letter(self):
        return col_to_letters(self.col)

