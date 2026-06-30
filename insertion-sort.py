# divide sequence into two sublists
# 1. sorted - length of 1
# 2. unsorted
# compare val to immediate left and change positions
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import time

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            # check left item and make sure not to go into negative indexing
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i] # swap
            i = i - 1 # look at next item

    return list_a

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Insertion Sort")
        self.geometry("800x700")

        # input box
        ttk.Label(self, text="Enter numbers seperated by a space:").pack(pady=5)
        self.input_box = ttk.Entry(self, width=40)
        self.input_box.pack(pady=5)

        # sort button
        ttk.Button(self, text="Sort", command=self.sort_array).pack(pady=10)

        # matplotlib visualization
        self.fig = Figure(figsize=(8, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # output box
        ttk.Label(self, text="Sorted Result: ").pack(pady=5)
        self.output_box = tk.Text(self, height=5, width=40)
        self.output_box.pack(pady=5)

    def draw_bars(self):
        self.ax.bar(range(len(self.data)))
    
    def sort_array(self):
        user_input = self.input_box.get()
        user_arr = user_input.split()

        result = insertion_sort(user_arr)
        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(1.0, f"Sorted: {result}")

if __name__ == "__main__":
    app = App()
    app.mainloop()