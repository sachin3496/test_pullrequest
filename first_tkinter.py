import tkinter as tk


root = tk.Tk()

root.title("Hello World Application")

label = tk.Label(text="Hello World", fg='#eeeeee', bg='#333333', height=10, width=30,
        font=('Times', 40, 'bold'))

label.pack(fill=tk.BOTH, expand=tk.YES)


root.mainloop()
