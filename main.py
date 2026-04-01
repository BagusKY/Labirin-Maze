from maze import Maze
from stack import Stack
from cell import CellPosition
from utils import read_pair, validate_maze_dimensions
from maze_generator import generate_maze, save_maze


# -------------------------
# BACA FILE MAZE
# -------------------------
# generate maze baru setiap run
maze_data, start, exit = generate_maze(15, 15)
save_maze("maze_input.txt", maze_data, start, exit)

def buildMaze(filename):
    with open(filename, "r") as f:
        # ukuran maze
        rows, cols = read_pair(f.readline())
        validate_maze_dimensions(rows, cols)
        maze = Maze(rows, cols)

        # start
        s_row, s_col = map(int, f.readline().split())
        start: CellPosition[int, int] = CellPosition(s_row, s_col)
        validate_maze_dimensions(rows, cols)
        maze.setStart(s_row, s_col)

        # exit
        e_row, e_col = map(int, f.readline().split())
        validate_maze_dimensions(rows, cols)
        maze.setExit(e_row, e_col)

        # isi maze
        for r in range(rows):
            line = f.readline().strip()
            for c in range(cols):
                if line[c] == "*":
                    maze.setWall(r, c)

    return maze


# -------------------------
# PROGRAM UTAMA
# -------------------------
def main():
    filename = "maze_input.txt"  # bisa kamu ubah

    maze = buildMaze(filename)
    stack = Stack()

    print("Maze Awal:")
    maze.draw()

    print("\nMencari jalur...\n")

    if maze.findPath(stack):
        print("Jalur ditemukan!\n")
    else:
        print("Tidak ada jalur!\n")

    print("Maze Hasil:")
    maze.draw()


# -------------------------
# ENTRY POINT
# -------------------------
if __name__ == "__main__":
    main()