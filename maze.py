class CellPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Maze:
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols

        # buat grid kosong
        self._mazeCells = [[None for _ in range(numCols)] for _ in range(numRows)]

        self._startCell = None
        self._exitCell = None

    # -------------------------
    # SETTER
    # -------------------------
    def setWall(self, row, col):
        self._mazeCells[row][col] = Maze.MAZE_WALL

    def setStart(self, row, col):
        self._startCell = CellPosition(row, col)

    def setExit(self, row, col):
        self._exitCell = CellPosition(row, col)

    # -------------------------
    # GETTER
    # -------------------------
    def numRows(self):
        return self._numRows

    def numCols(self):
        return self._numCols

    # -------------------------
    # VALIDASI GERAK
    # -------------------------
    def _validMove(self, row, col):
        return (
            0 <= row < self._numRows and
            0 <= col < self._numCols and
            self._mazeCells[row][col] is None
        )

    def _exitFound(self, row, col):
        return (
            row == self._exitCell.row and
            col == self._exitCell.col
        )

    # -------------------------
    # CARI JALUR (STACK)
    # -------------------------
    def findPath(self, stack):
        # push posisi awal
        stack.push((self._startCell.row, self._startCell.col))
        self._mazeCells[self._startCell.row][self._startCell.col] = Maze.PATH_TOKEN

        while not stack.isEmpty():
            row, col = stack.peek()

            # cek apakah sudah sampai exit
            if self._exitFound(row, col):
                return True

            # cek 4 arah
            moved = False
            directions = [
                (row - 1, col),  # atas
                (row + 1, col),  # bawah
                (row, col - 1),  # kiri
                (row, col + 1),  # kanan
            ]

            for r, c in directions:
                if self._validMove(r, c):
                    self._mazeCells[r][c] = Maze.PATH_TOKEN
                    stack.push((r, c))
                    moved = True
                    break

            # kalau buntu → backtracking
            if not moved:
                self._mazeCells[row][col] = Maze.TRIED_TOKEN
                stack.pop()

        return False

    # -------------------------
    # RESET
    # -------------------------
    def reset(self):
        for r in range(self._numRows):
            for c in range(self._numCols):
                if self._mazeCells[r][c] in (Maze.PATH_TOKEN, Maze.TRIED_TOKEN):
                    self._mazeCells[r][c] = None

    # -------------------------
    # TAMPILKAN MAZE
    # -------------------------
    def draw(self):
        for r in range(self._numRows):
            row_str = ""
            for c in range(self._numCols):
                if self._mazeCells[r][c] == Maze.MAZE_WALL:
                    row_str += "*"
                elif self._mazeCells[r][c] == Maze.PATH_TOKEN:
                    row_str += "x"
                elif self._mazeCells[r][c] == Maze.TRIED_TOKEN:
                    row_str += "o"
                else:
                    row_str += "."
            print(row_str)