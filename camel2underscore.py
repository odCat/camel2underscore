#!python3

input = ["TestInput1", "test2Input", "1test"]
out = ''

for i in input:
    for j in i:
        if j in ['0','1','2','3','4','5','6','7','8','9']:
            out = i[:i.find(j)]
            out += '_' + j + '_'
            out += i[i.find(j) + 1:]
    if out[0] == "_":
        out = out[1:]
    if out[-1] == "_":
        out = out[:-1]
    print(out)
