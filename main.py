import tkinter as tk
import tkinter.ttk as ttk



class MenuView(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self["padding"] = (10, 10)
		self["relief"] = "solid"
		ttk.Button(self, text="Menu Items").pack()


class PdfView(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(*args, **kwargs)
		ttk.Button(self, text="Pdf Preview").pack(side=tk.LEFT, fill=tk.BOTH)
		self["padding"] = (10, 10)
		self["relief"] = "solid"

class ToolsView(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(*args, **kwargs)
		ttk.Button(self, text="Tools View").pack(side=tk.RIGHT, fill=tk.BOTH)
		self["padding"] = (10, 10)
		self["relief"] = "solid"

class MainView(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(*args, **kwargs)
		print(str(self))
		print(str(parent))
		self["padding"] = (5, 10)
		# Frames
		MenuView(self).grid(sticky=(tk.E, tk.W), columnspan=2)
		PdfView(self).grid(row=1, column=0, sticky=(tk.E, tk.W, tk.S, tk.N))
		ToolsView(self).grid(row=1, column=1, sticky=(tk.E, tk.W, tk.S, tk.N))
		# 
		# self.columnconfigure(0, weight=1)
		# self.rowconfigure(0, weight=1)


class Application(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		print(str(self))
		self.title("PDF Editor")
		self.geometry("200x300")
		MainView(self).grid(sticky=(tk.S, tk.E, tk.N, tk.W))
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		# self.columnconfigure(1, weight=1)
		self.rowconfigure(1, weight=1)


if __name__ == "__main__":
	app = Application()
	app.mainloop()

