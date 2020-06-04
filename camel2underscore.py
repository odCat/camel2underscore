#!python3


def remove_newline(input):
    output = []
    for line in input:
        output.append(line[:-1])
    return output

def read_input_from_file():
    input = open('input_file.txt')
    return input.readlines()

def first_char_is_underline(output):
    return output[0] == '_'
def last_char_is_underline(output):
    return output[-1] == '_'
def remove_first_character(output):
    return output[1:]
def remove_last_character(output):
    return output[:-1]

def make_printable(output):
    if first_char_is_underline(output):
        output = remove_first_character(output)
    if last_char_is_underline(output):
        output = remove_last_character(output)
    return output.lower()

def convert(input_values):
    previous_was_digit = False
    previous_was_uppercase = False
    inside_acronym = False

    output = ''
    for value in input_values:
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
    return output[:-1]

input_values = remove_newline(read_input_from_file())
print(convert(input_values))

# TODO
# refactor
