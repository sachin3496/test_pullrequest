import tkinter as tk


root = tk.Tk()

fg = '#eeeeee'
bg = '#333333'
def change_color():
        global fg
        if fg == '#eeeeee':
                fg = '#333333'
                bg = '#eeeeee'
                label.config(fg=fg, bg=bg)
        else:
                fg = '#eeeeee'
                bg='#333333'
                label.config(fg=fg, bg=bg)
root.title("Hello World Application")

label = tk.Label(text="Hello World", fg='#eeeeee', bg='#333333', height=10, width=30,
        font=('Times', 40, 'bold'))

label.pack(fill=tk.BOTH, expand=tk.YES)

label.after(1000, change_color)

root.mainloop()
