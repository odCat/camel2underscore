#!python3

input_values = ["TestInput1", "Test2Input", "Test22Test", "TestThisTest", "1Is21NOT"]
previous_was_digit = False
previous_was_uppercase = False

def first_char_is_underline(output):
    return output[0] == '_'
def last_char_is_underline(output):
    return output[-1] == '_'

def make_printable(output):
    if first_char_is_underline(output):
        output = output[1:]
    if last_char_is_underline(output):
        output = output[:-1]
    print(output.lower())

for value in input_values:
    output = ''

    for char in value:
        if char.isdigit():
            if not previous_was_digit:
                output += '_'
            previous_was_digit = True
        elif char.isupper():
            if not previous_was_uppercase:
                output += '_'
            previous_was_uppercase = True
        else:
            previous_was_digit = previous_was_uppercase = False
        output += char

    make_printable(output)

# TODO
# refactor
