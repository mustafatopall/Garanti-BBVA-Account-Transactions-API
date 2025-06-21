import tkinter as tk
from tkinter import ttk

class DataDisplay:
    def __init__(self, data):
        self.data = data
        self.root = tk.Tk()
        self.root.title("Garanti BBVA İşlemler")

        self.columns = ("Müşteri Adı", "İşlem ID", "Tarih", "Tutar", "Açıklama")
        self.tree = ttk.Treeview(self.root, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def fill(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in self.data:
            self.tree.insert("", "end", values=(
                row["customerName"],
                row["transactionId"],
                row["transactionDate"],
                row["amount"],
                row["description"]
            ))

    def run(self):
        self.fill()
        self.root.mainloop()
