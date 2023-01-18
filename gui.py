#!python

#   Copyright 2020, 2021, 2022 Mihai Gătejescu
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


previous = ''


def set_input_text(text):
    text_input.delete(1.0, tk.END)
    text_input.insert(1.0, text)


def set_input_text_from_file():
    data = c2u.read_input_from_file()
    data = c2u.list_to_text(data)
    set_input_text(data)


def convert_input_camel_2_underscore():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.convert_camel_2_underscore(previous.split())
    set_input_text(data + '\n')


def convert_input_text_to_code():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.convert_text_to_code(previous)
    set_input_text(data.rstrip())


def convert_input_text_to_double_quote_list():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.to_double_quote_list(previous)
    set_input_text(data.rstrip())

def convert_input_text_to_single_quote_list():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.to_one_quote_list(previous)
    set_input_text(data.rstrip())

def convert_input_code_to_text():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.convert_to_text(previous)
    set_input_text(data.rstrip())


def switch_between_cases():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.switch_cases(previous)
    set_input_text(data.rstrip())


def convert_input_text_into_two_columns():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.split_into_two_columns(previous)
    set_input_text(data.rstrip())


def keep_only_first_column():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.get_first_column(previous)
    set_input_text(data.rstrip())


def sort_lines():
    global previous
    previous = text_input.get(1.0, tk.END)
    data = c2u.order_lines(previous)
    set_input_text(data.rstrip())


def replace_with_previous():
    global previous
    if previous != '':
        temp = text_input.get(1.0, tk.END)
        set_input_text(previous.rstrip())
        previous = temp


# Command frame
command_frame = tk.Frame(root)
command_frame.pack(side='right')
button1 = tk.Button(command_frame, text='Open Text File')
button1.pack(expand=tk.YES)
button2 = tk.Button(command_frame, text='Camel 2 Underscore')
button2.pack(expand=tk.YES)
button3 = tk.Button(command_frame, text='Comma-Separated Strings')
button3.pack(expand=tk.YES)
button4 = tk.Button(command_frame, text='List (double quotes)')
button4.pack(expand=tk.YES)
button5 = tk.Button(command_frame, text='List (single quotes)')
button5.pack(expand=tk.YES)
button6 = tk.Button(command_frame, text='Plain Text')
button6.pack(expand=tk.YES)
button7 = tk.Button(command_frame, text='Lower/Uppercase')
button7.pack(expand=tk.YES)
button8 = tk.Button(command_frame, text='Split into two columns')
button8.pack(expand=tk.YES)
button9 = tk.Button(command_frame, text='First column')
button9.pack(expand=tk.YES)
button10 = tk.Button(command_frame, text='Sort')
button10.pack(expand=tk.YES)
button11 = tk.Button(command_frame, text='Undo')
button11.pack(expand=tk.YES)

# Text frame
text_frame = tk.Frame(root)
text_frame.pack(side='left', fill='both', expand=True)
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side='right', fill='y')
text_input = tk.Text(text_frame, wrap='word', yscrollcommand=scrollbar.set)
text_input.pack(side='left', fill='both', expand=True)
scrollbar['command'] = text_input.yview

# Set commands
button1['command'] = (lambda: set_input_text_from_file())
button2['command'] = (lambda: convert_input_camel_2_underscore())
button3['command'] = (lambda: convert_input_text_to_code())
button4['command'] = (lambda: convert_input_text_to_double_quote_list())
button5['command'] = (lambda: convert_input_text_to_single_quote_list())
button6['command'] = (lambda: convert_input_code_to_text())
button7['command'] = (lambda: switch_between_cases())
button8['command'] = (lambda: convert_input_text_into_two_columns())
button9['command'] = (lambda: keep_only_first_column())
button10['command'] = (lambda: sort_lines())
button11['command'] = (lambda: replace_with_previous())

root.mainloop()

# TODO
# Maybe disable the buttons so an action cannot be taken
#  multiple times
# Use OOP
# Make tests
