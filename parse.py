with open('parse.v') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if line.__contains__('input'):
        print(line, end="")
        lines[i] = ""
    if i > 400:
        break

for i, line in enumerate(lines):
    if line.__contains__('output'):
        print(line, end="")
        lines[i] = ""
    if i > 400:
        break

file2 = open('sourted.v', 'w+')

for line in lines:
    file2.write(line)

file2.close()


    
