import tkinter as tk

root = tk.Tk()
flag = True

def change_color():
    global flag
    if flag:
        label.config(fg ='#333333',bg = '#eeeeee')
        flag = False
    else:
        label.config(fg = '#eeeeee', bg='#333333')
        flag = True
    label.after(1000, change_color)
root.title("Hello World Application")

label = tk.Label(text="Hello World", fg='#eeeeee', bg='#333333', height=10, width=30,
        font=('Times', 40, 'bold'))
label.pack(fill=tk.BOTH, expand=tk.YES)

exit_button = tk.Button(root, text='Exit', fg='red', bg='#eeeeee', font=('monospace', 24, 'bold'))
exit_button.pack(fill=tk.X, expand=tk.YES)
exit_button.config(command=lambda : root.quit())

label.after(1000, change_color)

root.mainloop()
