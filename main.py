import tkinter as tk
import tkinter.ttk as ttk



class MenuView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self["relief"] = "groov"
        self["padding"] = 10
        # this will be menu
        ttk.Label(self, text="Menu Items goes here!").pack()


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

        MenuView(self).grid(row=0, column=0, sticky=(tk.E, tk.W), columnspan=2)
        PdfView(self).grid(row=1, column=0, sticky=(tk.S, tk.N, tk.E, tk.W))
        OpFrame(self).grid(row=1, column=1, sticky=(tk.S, tk.N, tk.E, tk.W))

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)



class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("400x300")
        MainView(self).pack(expand=True, fill='both')
        self.columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()
