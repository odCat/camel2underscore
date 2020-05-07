#!python3

input = ["TestInput1", "Test2Input", "1Test", "Test22Test", "TestThisTest"]

for i in input:
    output = ''

    for j in i:
        if j > '0' and j < '9':
            output += '_' + j
        elif j.isupper():
            output += '_' + j
        else:
            output += j

    if output[0] == "_":
        output = output[1:]
    if output[-1] == "_":
        output = output[:-1]
    print(output.lower())

# TODO
# Fis the multiple digits number
