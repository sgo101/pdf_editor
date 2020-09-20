import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox



class MainMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._file_menu()
        self._edit_menu()
        self._help_menu()

    def _file_menu(self):
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(label="Open", command=self.open)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_command(label="Exit", command=sys.exit)
        # display File menu items
        self.add_cascade(label="File", menu=file_menu)

    def _edit_menu(self):
        edit_menu = tk.Menu(self, tearoff=False)
        edit_menu.add_command(label="Insert Image", command=self.insert_image)
        self.add_cascade(label="Edit", menu=edit_menu)

    def _help_menu(self):
        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(label="Help", command=self.help_msg)
        help_menu.add_command(label="Contact", command=self.contact)
        self.add_cascade(label="Help", menu=help_menu)


    def open(self):
        print("open menu item clicked!") 

    def save_as(self):
        pass

    def insert_image(self):
        pass

    def help_msg(self):
        msgbox.showinfo("helo", "HELP!!!!")

    def contact(self):
        pass


class PdfView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self["relief"] = "solid"
        self["padding"] = 10
        ttk.Label(self, text="In Center Frame").pack()


class OpFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self["relief"] = "sunken"
        self["padding"] = 10
        ttk.Label(self, text="In Left Frame").grid()


class MainView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self["padding"] = 10
        self["relief"] = "solid"

        PdfView(self).grid(row=1, column=0, sticky=(tk.S, tk.N, tk.E, tk.W))
        OpFrame(self).grid(row=1, column=1, sticky=(tk.S, tk.N, tk.E, tk.W))

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

2
class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("400x300")
        MainView(self).pack(expand=True, fill='both')
        menubar = MainMenu(self)
        self.config(menu=menubar)


        self.columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()
