#!python3

input_values = ["TestInput1", "Test2Input", "1Test", "Test22Test", "TestThisTest", "Is21NOT"]
digit_flag = False
upper_flag = False

for i in input:
    output = ''

    for j in i:
        if j.isdigit():
            if not digit_flag:
                output += '_'
            digit_flag = True
        elif j.isupper():
            if not upper_flag:
                output += '_'
            upper_flag = True
        else:
            digit_flag = upper_flag = False
        output += j

    if output[0] == "_":
        output = output[1:]
    if output[-1] == "_":
        output = output[:-1]
    print(output.lower())

# TODO
# refactor
