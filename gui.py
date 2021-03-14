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

import camel2underscore as c2u

root = tk.Tk()
root.geometry('400x800')
root.title('Camel to underscore')


def set_input_text(text):
    text_input.delete(1.0, tk.END)
    text_input.insert(1.0, text)


def set_text_from_file():
    data = c2u.read_input_from_file()
    data = c2u.list_to_text(data)
    set_input_text(data)


def convert_input():
    data = text_input.get(1.0, tk.END)
    data = c2u.convert_camel_2_underline(data.split())
    set_input_text(data + '\n')


def convert_input_text_to_code():
    data = text_input.get(1.0, tk.END)
    data = c2u.convert_text_to_code(data)
    set_input_text(data.rstrip())


def convert_input_code_to_text():
    data = text_input.get(1.0, tk.END)
    data = c2u.convert_code_to_text(data)
    set_input_text(data.rstrip())


# Command frame
command_frame = tk.Frame(root)
command_frame.pack(side='right')
button1 = tk.Button(command_frame, text='Open Text File')
button1.pack(expand=tk.YES)
button2 = tk.Button(command_frame, text='Convert')
button2.pack(expand=tk.YES)
button3 = tk.Button(command_frame, text='To Code')
button3.pack(expand=tk.YES)
button4 = tk.Button(command_frame, text='To Text')
button4.pack(expand=tk.YES)

# Text frame
text_frame = tk.Frame(root)
text_frame.pack(side='left', fill='both', expand=True)
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side='right', fill='y')
text_input = tk.Text(text_frame, wrap='word',
                     yscrollcommand=scrollbar.set)
text_input.pack(side='left', fill='both', expand=True)
scrollbar['command'] = text_input.yview

# Set commands
button1['command'] = (lambda: set_text_from_file())
button2['command'] = (lambda: convert_input())
button3['command'] = (lambda: convert_input_text_to_code())
button4['command'] = (lambda: convert_input_code_to_text())

root.mainloop()

# TODO
# Maybe disable the buttons so an action cannot be taken
# multiple times
