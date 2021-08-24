import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import _flatten

class GUI(tk.Frame):
	dataset = []
	
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)
		self.master.title('CalPL 0.1')
		self.master.geometry('400x400')
		self.create_widgets()
		return
	
	def create_widgets(self):
		# Button
		self.b_plot = tk.Button(self.master, text = 'Plot', width = 6, height = 2, font = ("Arial", 60), command = self.plot)
		self.b_plot.place(x = 200,y = 220,anchor = 'center')
		self.l_color = tk.Label(self.master, text = 'Color:', width = 8, height = 1,font = ("Arial", 20))
		self.l_color.place(x = 80, y = 50, anchor = 'center')
		self.cmb_color = ttk.Combobox(self.master, width = 8, height = 1,font = ("Arial", 20))
		self.cmb_color['value'] = ('Greys', 'Jet')
		self.cmb_color.current(1)
		self.cmb_color.place(x = 200, y = 50, anchor = 'center')
		return
	
	def line2list(self, f, c2m = 'String'):
		linetemp = f.readline()
		datalist = linetemp.strip().split()
		if c2m == 'Int':
			datalist = list(map(int, datalist))
		elif c2m == 'Float32':
			datalist = list(map(eval, datalist))
		return datalist
	
	def load(self):
		f = open('data.txt', 'r')
		linetemp = self.line2list(f, 'Float32')
		self.dataset.append(linetemp)
		data_size = len(linetemp)
		for i in range(data_size - 1):
			linetemp = self.line2list(f, 'Float32')
			self.dataset.append(linetemp)
		f.close()
		return
		
	def plot(self):
		self.dataset.clear()
		self.load()
		self.plot_res()
		return

	def plot_res(self):
		plt.imshow(self.dataset, cmap='jet')
		plt.show(block = False)
		return
		
root = tk.Tk()
app = GUI(root)

app.mainloop()