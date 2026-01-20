import sqlite3
import tkinter as tk
from tkinter import ttk
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


DB_NAME = resource_path("Library_items.db")


class LibraryExplorerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LibraryPy")
        self.root.geometry("1100x650")

        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

        self.build_layout()
        self.load_tags()

    def build_layout(self):
        main = ttk.Frame(self.root, padding=10)
        main.pack(fill="both", expand=True)

        main.columnconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)
        main.columnconfigure(2, weight=2)

        # Tags
        tag_frame = ttk.LabelFrame(main, text="Topics")
        tag_frame.grid(row=0, column=0, sticky="nsew", padx=5)

        self.tag_list = tk.Listbox(tag_frame)
        self.tag_list.pack(fill="both", expand=True)
        self.tag_list.bind("<<ListboxSelect>>", self.on_tag_select)

        # Libraries
        lib_frame = ttk.LabelFrame(main, text="Libraries")
        lib_frame.grid(row=0, column=1, sticky="nsew", padx=5)

        self.lib_list = tk.Listbox(lib_frame)
        self.lib_list.pack(fill="both", expand=True)
        self.lib_list.bind("<<ListboxSelect>>", self.on_library_select)

        # Items
        item_frame = ttk.LabelFrame(main, text="Functions and Tools")
        item_frame.grid(row=0, column=2, sticky="nsew", padx=5)

        self.item_text = tk.Text(item_frame, wrap="word")
        self.item_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(item_frame, command=self.item_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.item_text.config(yscrollcommand=scrollbar.set)

        self.item_text.tag_configure("title", font=("Segoe UI", 10, "bold"))
        self.item_text.config(state="disabled")

    def load_tags(self):
        self.tag_list.delete(0, tk.END)
        self.cursor.execute("SELECT id, tag FROM tags ORDER BY tag;")
        self.tags = self.cursor.fetchall()

        for _, tag in self.tags:
            self.tag_list.insert(tk.END, tag)

    def on_tag_select(self, event):
        if not self.tag_list.curselection():
            return

        index = self.tag_list.curselection()[0]
        tag_id = self.tags[index][0]

        self.cursor.execute("""
        SELECT l.id, l.name
        FROM library l
        JOIN library_tags lt ON l.id = lt.library_id
        WHERE lt.tag_id = ?
        ORDER BY l.name;
        """, (tag_id,))

        self.libraries = self.cursor.fetchall()

        self.lib_list.delete(0, tk.END)
        self.item_text.config(state="normal")
        self.item_text.delete("1.0", tk.END)
        self.item_text.config(state="disabled")

        for _, name in self.libraries:
            self.lib_list.insert(tk.END, name)

    def on_library_select(self, event):
        if not self.lib_list.curselection():
            return

        index = self.lib_list.curselection()[0]
        library_id = self.libraries[index][0]

        self.cursor.execute("""
        SELECT name, description, example
        FROM items
        WHERE library_id = ?
        ORDER BY name;
        """, (library_id,))

        items = self.cursor.fetchall()

        self.item_text.config(state="normal")
        self.item_text.delete("1.0", tk.END)

        for name, desc, example in items:
            self.item_text.insert(tk.END, name + "\n", "title")
            if desc:
                self.item_text.insert(tk.END, "  " + desc + "\n")
            if example:
                self.item_text.insert(tk.END, "  Example\n")
                for line in example.split("\n"):
                    self.item_text.insert(tk.END, "    " + line + "\n")
            self.item_text.insert(tk.END, "\n")

        self.item_text.config(state="disabled")

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryExplorerGUI(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (app.close(), root.destroy()))
    root.mainloop()
