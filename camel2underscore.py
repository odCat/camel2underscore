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
import re
from sys import argv
from sys import path
from sys import exit as sys_exit
from re import sub
import os
import json


def is_underscore_notation(value):
    return '_' in value


def first_char_is_underscore(output):
    return output[0] == '_'


def last_char_is_underscore(output):
    return output[-1] == '_'


def remove_first_character(output):
    return output[1:]


def remove_last_character(output):
    return output[:-1]


def remove_underscores_from_start_and_end(output):
    while first_char_is_underscore(output):
        output = remove_first_character(output)
    while last_char_is_underscore(output):
        output = remove_last_character(output)
    return output.lower()


def read_input_from_file(input_file='input_file.txt'):
    output = []

    def remove_newlines_from_list(text):
        result = []
        for line in text:
            result.append(remove_last_character(line))
        return result

    try:
        input_file = open(os.path.join(path[0], input_file))
        output = input_file.readlines()
        input_file.close()
        output = remove_newlines_from_list(output)
    except FileNotFoundError:
        print('File not found')
        sys_exit()
    return output


def convert_text_to_code(text):
    result = sub('\n+', '\n', text)
    result = "'" + result
    result = result.replace('\n', "',\n'")
    return result[:-3] + '\n'


def list_to_text(a_list):
    result = ''
    for i in a_list:
        result += i + '\n'
    return result


def remove_whitespaces(plain_text):
    plain_text = plain_text.replace('\t', '')
    plain_text = sub('\n+', '\n', plain_text)
    plain_text = sub(' +\n', '\n', plain_text)
    plain_text = sub('\n +', '\n', plain_text)
    return plain_text.lstrip()

def to_test_list(text):
    result = remove_whitespaces(text)
    result = result.replace('\n', '", "')
    return '["' + result[:-3] + ']'


def convert_to_text(data):

    def remove(text, characters):
        for ch in characters:
            text = text.replace(ch, '')
        return text

    result = data.replace('\'', '"')
    result = result.replace('\n', '')
    result = result.replace('", ', '\n')
    result = result.replace('",', '\n')
    result = remove(result, '[]"')
    return result


def convert_camel_2_underscore(input_values_list):
    previous_was_digit = False
    previous_was_uppercase = False
    inside_acronym = False

    output = ''
    for value in input_values_list:
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
            line = remove_underscores_from_start_and_end(line)
        output += line + '\n'
    return remove_last_character(output)


def list_to_lowercase(columns):
    result = []
    for i in columns:
        result.append(i.lower())
    return result


def compare_columns(columns1, columns2):
    columns1 = list_to_lowercase(columns1)
    columns2 = list_to_lowercase(columns2)
    return set(columns1) == set(columns2)


def get_and_compare_columns(source1, source2):
    def get_columns(source):
        with open(source, 'r') as source:
            result = json.load(source)
        return result

    columns1 = get_columns(source1)
    columns2 = get_columns(source2)
    return compare_columns(columns1, columns2)


def split_into_two_columns(text, items_in_column=2):
    text = sub('^ *', '', text)
    text = sub(' +', ' ', text)
    result = ''
    count = 0
    for character in text:
        if character == ' ':
            count += 1
            if count == items_in_column:
                count = 0
                character = '\n'
        result += character

    return result


def get_first_column(text):
    text = remove_whitespaces(text)
    return sub(' .*$', '', text, flags=re.MULTILINE)


if __name__ == '__main__':
    if len(argv) > 1:
        input_values = read_input_from_file(argv[1])
    else:
        input_values = read_input_from_file()
    print(convert_camel_2_underscore(input_values))

# TODO
# Check if the values are not already underscored
# ^ this will need logging
# Include help functionality
