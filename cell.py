class CellPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    # -------------------------
    # REPRESENTASI STRING
    # -------------------------
    def __repr__(self):
        return f"Cell({self.row}, {self.col})"

    # -------------------------
    # CEK KESAMAAN POSISI
    # -------------------------
    def __eq__(self, other):
        if not isinstance(other, CellPosition):
            return False
        return self.row == other.row and self.col == other.col

    # -------------------------
    # HASH (AGAR BISA DIPAKAI DI SET/DICT)
    # -------------------------
    def __hash__(self):
        return hash((self.row, self.col))