import tkinter as tk
from tkinter.ttk import *
import random

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self._master = master
		self.result_text = ""
		self.first_roll = 0
		self.hist0 = 0
		self.hist1 = 0
		self.hist2 = 0
		self.hist3 = 0
		self.create_widgets()
		

	def create_widgets(self):
		"""
		Creates the buttons and input areas.
		"""
		tk.Label(self._master, text="How many?").grid(row=0)
		self.to_set = tk.Label(self._master, text=self.result_text)
		self.to_set.grid(row=7, columnspan=2)
		self.rolled = tk.Label(self._master, text="")
		self.rolled.grid(row=8, columnspan=2)
		self.history = tk.Label(self._master, text="")
		self.history.grid(row=9, columnspan=2)
		self.text1 = tk.Entry(self._master)
		self.text1.grid(row=0, column=1)
		self.button = tk.Button(text='d4', command=self.result_d4, width=15).grid(row=2, column=0)
		self.button = tk.Button(text='d6', command=self.result_d6, width=15).grid(row=2, column=1)
		self.button = tk.Button(text='d8', command=self.result_d8, width=15).grid(row=3, column=0)
		self.button = tk.Button(text='d10', command=self.result_d10, width=15).grid(row=3, column=1)
		self.button = tk.Button(text='d12', command=self.result_d12, width=15).grid(row=4, column=0)
		self.button = tk.Button(text='d20', command=self.result_d20, width=15).grid(row=4, column=1)

	def result(self, die):
		"""
		Calculates the result given the two input numbers.
		"""
		try:
			x = int(self.text1.get())
			if x == 0:
				self.to_set['text'] = "You rolled no dice."
				self.rolled['text'] = ""
			else:
				y = die
				result = 0
				self.rolled['text'] = ""
				num = random.randint(1, y)
				result += num
				self.first_roll += 1
				if x == 1:
					self.rolled['text'] += str(num)
				else:
					self.rolled['text'] += str(num) + "+"
				for dice in range(2, x+1):
					if x == dice:
						num = random.randint(1, y)
						result += num
						self.rolled['text'] += str(num)						
					else:
						num = random.randint(1, y)
						result += num
						self.rolled['text'] += "" + str(num) + "+"
				self.result_text = "Result: " + str(result) + "."
				self.to_set['text'] = self.result_text
				#history section
				self.hist3 = self.hist2
				self.hist2 = self.hist1
				self.hist1 = self.hist0
				self.hist0 = str(result)
				if self.first_roll == 2:
					self.history['text'] = "History: " + str(self.hist1)
				elif self.first_roll == 3:
					self.history['text'] = "History: " + str(self.hist1) + ", " + str(self.hist2)
				elif self.first_roll > 3:
					self.history['text'] = "History: " + str(self.hist1) + ", " + str(self.hist2) + ", " + str(self.hist3)
		except ValueError:
			self.to_set['text'] = "Please enter a number."

	def result_d4(self):
		self.result(4)
	def result_d6(self):
		self.result(6)
	def result_d8(self):
		self.result(8)
	def result_d10(self):
		self.result(10)
	def result_d12(self):
		self.result(12)
	def result_d20(self):
		self.result(20)


#create window
#with two input spaces
#with text "Please enter 2 numbers. A number in this range will be produced."
window = tk.Tk()
window.title("Dice")
canvas = tk.Canvas(window, width=600, height=800)
app = Application(window)
app.mainloop()

#display result
