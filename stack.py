class Stack:
    def __init__(self):
        self._items = []

    # -------------------------
    # CEK KOSONG
    # -------------------------
    def isEmpty(self):
        return len(self._items) == 0

    # -------------------------
    # JUMLAH ELEMEN
    # -------------------------
    def __len__(self):
        return len(self._items)

    # -------------------------
    # LIHAT ELEMEN TERATAS
    # -------------------------
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack kosong, tidak bisa peek")
        return self._items[-1]

    # -------------------------
    # AMBIL (POP)
    # -------------------------
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack kosong, tidak bisa pop")
        return self._items.pop()

    # -------------------------
    # TAMBAH (PUSH)
    # -------------------------
    def push(self, item):
        self._items.append(item)

    # -------------------------
    # DEBUG (OPSIONAL)
    # -------------------------
    def __str__(self):
        return f"Stack({self._items})"