import random


def generate_maze(rows, cols):
    # pastikan ukuran minimal
    if rows < 3 or cols < 3:
        raise ValueError("Ukuran maze minimal 3x3")

    # buat grid penuh dinding
    maze = [["*" for _ in range(cols)] for _ in range(rows)]

    # start & exit
    start = (1, 1)
    exit = (rows - 2, cols - 2)

    # arah gerak (2 langkah biar ada ruang)
    directions = [
        (-2, 0),
        (2, 0),
        (0, -2),
        (0, 2)
    ]

    def is_valid(r, c):
        return 0 < r < rows-1 and 0 < c < cols-1

    def carve_path(r, c):
        maze[r][c] = "."

        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if is_valid(nr, nc) and maze[nr][nc] == "*":
                # buka jalan di tengah
                maze[r + dr // 2][c + dc // 2] = "."
                carve_path(nr, nc)

    # mulai dari start
    carve_path(start[0], start[1])

    return maze, start, exit


def save_maze(filename, maze, start, exit):
    rows = len(maze)
    cols = len(maze[0])

    with open(filename, "w") as f:
        f.write(f"{rows} {cols}\n")
        f.write(f"{start[0]} {start[1]}\n")
        f.write(f"{exit[0]} {exit[1]}\n")

        for row in maze:
            f.write("".join(row) + "\n")


# -------------------------
# TEST GENERATOR
# -------------------------
if __name__ == "__main__":
    maze, start, exit = generate_maze(15, 15)
    save_maze("maze_input.txt", maze, start, exit)
    print("Maze berhasil dibuat!")