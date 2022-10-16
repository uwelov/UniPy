
import tkinter as tk
window = tk.Tk()
window.geometry("400x200")
window.title("some title")
label = tk.Label(window, text = "Hello world")
label.place(x=100, y=100)
butClo = tk.Button(text='Закрыть', command=exit, font='serif 10')
butClo.grid(row=1, column=3, ipadx=0, ipady=5, padx=0, pady=5)
window.mainloop()
