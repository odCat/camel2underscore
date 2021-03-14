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

from sys import argv
from sys import path
from sys import exit as sys_exit
import os


def first_char_is_underline(output):
    return output[0] == '_'


def last_char_is_underline(output):
    return output[-1] == '_'


def remove_first_character(output):
    return output[1:]


def remove_last_character(output):
    return output[:-1]


def make_printable(output):
    while first_char_is_underline(output):
        output = remove_first_character(output)
    while last_char_is_underline(output):
        output = remove_last_character(output)
    return output.lower()


def read_input_from_file(input_file='input_file.txt'):
    output = []

    def remove_newlines_from_list(input):
        result = []
        for line in input:
            result.append(remove_last_character(line))
        return result

    try:
        input = open(os.path.join(path[0], input_file))
        output = input.readlines()
        output = remove_newlines_from_list(output)
        input.close()
    except FileNotFoundError:
        print('File not found')
        sys_exit()
    return output


def is_underscore_notation(value):
    return '_' in value


def convert_camel_2_underline(input_values):
    previous_was_digit = False
    previous_was_uppercase = False
    inside_acronym = False

    output = ''
    for value in input_values:
        if is_underscore_notation(value):
            continue
        line = ''

        for char in value:
            if char.isdigit():
                if not previous_was_digit:
                    line += '_'
                previous_was_digit = True
            elif char.isupper():
                if not previous_was_uppercase:
                    line += '_'
                else:
                    inside_acronym = True
                previous_was_uppercase = True
            elif char.islower():
                if inside_acronym:
                    line = line[:-1] + '_' + line[-1:]
                previous_was_uppercase = False
                previous_was_digit = False
                inside_acronym = False
            line += char
            line = make_printable(line)
        output += line + '\n'
    return remove_last_character(output)


if __name__ == '__main__':
    if len(argv) > 1:
        input_values = read_input_from_file(argv[1])
    else:
        input_values = read_input_from_file()
    print(convert_camel_2_underline(input_values))

# TODO
# check if the values are not already underscored
# ^ this will need logging
