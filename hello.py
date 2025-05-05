import tkinter as tk
from tkinter import filedialog, messagebox
import os


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("600x400")

        # Initial file path (None if no file is open)
        self.file_path = None

        # Text widget for content editing
        self.text_area = tk.Text(root, wrap="word", undo=True)
        self.text_area.pack(expand="true", fill="both")

        # Adding Menu Bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.create_menus()

    def create_menus(self):
        # Create 'File' menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        # Create 'Edit' menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Redo", command=self.redo_action)

    def new_file(self):
        """Create a new file"""
        if self.text_area.get(1.0, "end-1c"):
            if messagebox.askyesno("Save?", "Do you want to save changes?"):
                self.save_file()
        self.text_area.delete(1.0, "end-1c")
        self.file_path = None
        self.root.title("Simple Notepad - New File")

    def open_file(self):
        """Open an existing file"""
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.file_path = file_path
            self.root.title(f"Simple Notepad - {os.path.basename(file_path)}")
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, "end-1c")
                self.text_area.insert("insert", content)

    def save_file(self):
        """Save the current file"""
        if not self.file_path:
            self.save_as()
        else:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end-1c"))
            messagebox.showinfo("Success", f"File saved as {os.path.basename(self.file_path)}")

    def save_as(self):
        """Save the current file as a new file"""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.file_path = file_path
            self.save_file()

    def exit_app(self):
        """Exit the app"""
        if self.text_area.get(1.0, "end-1c"):
            if messagebox.askyesno("Save?", "Do you want to save changes?"):
                self.save_file()
        self.root.quit()

    def undo_action(self):
        """Undo the last action"""
        self.text_area.edit_undo()

    def redo_action(self):
        """Redo the last undone action"""
        self.text_area.edit_redo()


if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
