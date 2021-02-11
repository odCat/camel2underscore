#!python

import tkinter as tk

root = tk.Tk()
root.geometry('400x800')
root.title('Camel to underscore')

frame1 = tk.Frame(root)
frame1.pack(side = 'right')
button = tk.Button(frame1, text = 'Convert')
button.pack(side = 'right')

frame2 = tk.Frame(root)
frame2.pack(side = 'left', fill = 'both', expand = True)
scrollbar = tk.Scrollbar(frame2)
scrollbar.pack(side = 'right', fill = 'y')
text = tk.Text(frame2, wrap = 'word', yscrollcommand = scrollbar.set)
text.pack(side = 'left', fill = 'both', expand = True)
scrollbar['command'] = text.yview

root.mainloop()
