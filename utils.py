def read_pair(line):
    """
    Membaca dua angka dari satu baris string
    Contoh: "4 1" → (4, 1)
    """
    parts = line.strip().split()
    if len(parts) != 2:
        raise ValueError("Format harus 2 angka dipisahkan spasi")
    return int(parts[0]), int(parts[1])


def validate_maze_dimensions(rows, cols):
    """
    Validasi ukuran maze
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("Ukuran maze harus lebih dari 0")


def validate_position(row, col, rows, cols):
    """
    Validasi posisi start/exit
    """
    if not (0 <= row < rows and 0 <= col < cols):
        raise ValueError(f"Posisi ({row},{col}) di luar batas maze")


def print_separator():
    """
    Hanya untuk mempercantik output
    """
    print("=" * 40)


def debug_print(message, enable=False):
    """
    Debug optional (tidak mengganggu output utama)
    """
    if enable:
        print(f"[DEBUG] {message}")