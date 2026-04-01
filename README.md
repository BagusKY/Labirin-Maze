# 📄 README.md

```markdown
# 🧩 Maze Solver with Stack (Backtracking Algorithm)

> Implementasi penyelesaian labirin menggunakan **Struktur Data Stack (LIFO)** dan algoritma **Backtracking (DFS)** dalam Python.

---

## 📌 Deskripsi Project

Project ini merupakan implementasi konsep **Struktur Data Tumpukan (Stack)** untuk menyelesaikan permasalahan pencarian jalur dalam labirin (maze).  
Algoritma bekerja dengan teknik **Depth-First Search (DFS)** menggunakan Stack secara eksplisit (tanpa rekursi).

Program akan:
- Membaca labirin dari file
- Menentukan titik awal (start) dan tujuan (exit)
- Menelusuri jalur menggunakan Stack
- Menandai jalur benar dan jalan buntu

---

## 🧠 Konsep yang Digunakan

- **Stack (LIFO - Last In First Out)**
- **Backtracking**
- **Depth-First Search (DFS)**
- **Grid-based Pathfinding**
- **Modular Programming (Python)**

---

## ⚙️ Cara Kerja Algoritma

1. Push posisi awal ke dalam stack
2. Selama stack tidak kosong:
   - Ambil posisi teratas (peek)
   - Jika sudah sampai exit → selesai
   - Jika belum:
     - Coba 4 arah (atas, bawah, kiri, kanan)
     - Jika valid → push ke stack
     - Jika buntu → pop (mundur/backtrack)
3. Tandai:
   - `x` → jalur benar
   - `o` → jalan buntu

---

## 📂 Struktur Project

```

maze-solver-stack-python/
│
├── maze.py              # Logic utama maze & pathfinding
├── stack.py             # Implementasi Stack ADT
├── cell.py              # Representasi posisi (opsional OOP)
├── main.py              # Entry point program
├── utils.py             # Helper & validasi
├── maze_generator.py    # Generator maze random (advanced)
├── maze_input.txt       # Input maze
└── README.md            # Dokumentasi project

```

---

## 🧪 Format File Input (`maze_input.txt`)

```

5 5        # jumlah baris & kolom
4 1        # start (row col)
3 4        # exit (row col)

---

*.*.*
*...*
*.*..
*.***

````

### Keterangan:
- `*` → dinding
- `.` → jalan
- `x` → jalur benar (output)
- `o` → jalan buntu (output)

---

## 🚀 Cara Menjalankan Program

### 1. Clone Repository
```bash
git clone https://github.com/username/maze-solver-stack-python.git
cd maze-solver-stack-python
````

### 2. Jalankan Program

```bash
python main.py
```

---

## 🎲 Fitur Tambahan (Advanced)

### 🔹 Random Maze Generator

Program dapat menghasilkan labirin acak yang **pasti solvable**:

```python
from maze_generator import generate_maze, save_maze

maze_data, start, exit = generate_maze(15, 15)
save_maze("maze_input.txt", maze_data, start, exit)
```

---

## 📊 Kompleksitas

| Operasi        | Kompleksitas |
| -------------- | ------------ |
| Push / Pop     | O(1)         |
| Traversal Maze | O(n × m)     |

---

## ⚠️ Catatan Penting

* Algoritma menggunakan **DFS (Stack)**
  → **tidak menjamin jalur terpendek**

* Untuk jalur terpendek:

  * gunakan **BFS (Queue)**
  * atau **A***

---

## 🧠 Insight Akademik

Project ini menunjukkan implementasi nyata dari:

* Abstract Data Type (ADT)
* Problem Solving berbasis struktur data
* Representasi graf dalam bentuk grid
* Teknik eksplorasi state space

---

## 🔥 Pengembangan Selanjutnya

Beberapa upgrade yang bisa dilakukan:

* [ ] Visualisasi langkah demi langkah
* [ ] Perbandingan DFS vs BFS
* [ ] GUI berbasis Tkinter / Pygame
* [ ] Maze solver berbasis AI (A*)
* [ ] Export hasil ke file

---

## 👨‍💻 Author

**BagusKY**
Mahasiswa | Computer Science Enthusiast

---

## 📜 License

Project ini dibuat untuk keperluan pembelajaran dan pengembangan pribadi.

