file = open('day1input.txt', 'r')
instr = file.read()

# Part 1
floor = 0
for instruction in instr:
    if instruction == '(':
        floor += 1
    if instruction == ')':
        floor -= 1
        if floor < 0:
            break

print(floor)

# Part 2
floor = 0
for i in range(len(instr)):
    if instr[i] == '(':
        floor += 1
    if instr[i] == ')':
        floor -= 1
        if floor < 0:
            print(i + 1)
            break