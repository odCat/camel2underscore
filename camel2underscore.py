#!python3

input_values = ["TestInput1", "Test2Input", "Test22Test", "TestThisTest", "1Is21NOT"]
is_digit = False
is_uppercase = False

def make_printable(output):
    if output[0] == "_":
        output = output[1:]
    if output[-1] == "_":
        output = output[:-1]
    print(output.lower())

for value in input_values:
    output = ''

    for char in value:
        if char.isdigit():
            if not is_digit:
                output += '_'
            is_digit = True
        elif char.isupper():
            if not is_uppercase:
                output += '_'
            is_uppercase = True
        else:
            is_digit = is_uppercase = False
        output += char

    make_printable(output)

# TODO
# refactor
