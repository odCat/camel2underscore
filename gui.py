#!python

#   Copyright 2020, 2021 Mihai Gătejescu
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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
text = tk.Text(frame2, wrap = 'word')#, yscrollcommand = scrollbar.set)
text.pack(side = 'left', fill = 'both', expand = True)
#scrollbar['command'] = text.yview

root.mainloop()
