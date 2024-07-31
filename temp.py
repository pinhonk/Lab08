import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Untitled - Notepad")
        self.iconbitmap("icon.ico") 
        # Create menu bar
        self.main_menu = tk.Menu(self)

        # File menu
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)

        # Edit menu
        self.edit_menu = tk.Menu(self.main_menu, tearoff=0)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.undo_text)
        self.edit_menu.add_command(label="Redo", command=self.redo_text)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)

        # Help menu
        self.help_menu = tk.Menu(self.main_menu, tearoff=0)
        self.help_menu.add_command(label="About Notepad", command=self.show_about)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)

        self.config(menu=self.main_menu)

        # Create text area
        self.text_display = tk.Text(self)
        self.text_display.pack(fill="both", expand=True)

    # File menu functions
    def new_file(self):
        self.text_display.delete("1.0", tk.END)
        self.title("Untitled - Notepad")

    def open_file(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            try:
                with open(filename, "r") as f:
                    self.text_display.delete("1.0", tk.END)
                    self.text_display.insert("1.0", f.read())
                    self.title(f"{filename} - Notepad")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to open file: {e}")

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            try:
                with open(filename, "w") as f:
                    f.write(self.text_display.get("1.0", tk.END).strip())  # Strip newlines at the end
                    self.title(f"{filename} - Notepad")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to save file: {e}")

    # Edit menu functions
    def copy_text(self):
        try:
            self.text_display.clipboard_clear()
            self.text_display.clipboard_append(self.text_display.selection_get())
        except tk.TclError:
            messagebox.showwarning("Warning", "No text selected to copy.")

    def paste_text(self):
        try:
            self.text_display.insert(tk.INSERT, self.text_display.clipboard_get())
        except tk.TclError:
            messagebox.showwarning("Warning", "Clipboard is empty.")

    def cut_text(self):
        try:
            self.copy_text()
            self.text_display.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            messagebox.showwarning("Warning", "No text selected to cut.")

    def undo_text(self):
        try:
            self.text_display.edit_undo()
        except tk.TclError:
            messagebox.showwarning("Warning", "Nothing to undo.")

    def redo_text(self):
        try:
            self.text_display.edit_redo()
        except tk.TclError:
            messagebox.showwarning("Warning", "Nothing to redo.")

    def show_about(self):
        messagebox.showinfo("About Notepad", "This is a simple Notepad application.\nDeveloped by: [Your Name]")

if __name__ == "__main__":
    app = Notepad()
    app.mainloop()
