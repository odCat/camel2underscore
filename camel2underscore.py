#!python3

input = ["TestInput1", "test2Input", "1test"]
output = ''

for i in input:
    for j in i:
        if j in ['0','1','2','3','4','5','6','7','8','9']:
            output = i[:i.find(j)]
            output += '_' + j + '_'
            output += i[i.find(j) + 1:]
    if output[0] == "_":
        output = output[1:]
    if output[-1] == "_":
        output = output[:-1]
    print(output.lower())

# TODO
# Fis the multiple digits number
