origin = (0,0)
file = open('day3input.txt', 'r')
directions = file.read()

houses = set()
houses.add(origin)

# Part 1
curr_loc = [0, 0]
for direction in directions:
    if direction == '>':
        curr_loc[1] += 1
    if direction == '<':
        curr_loc[1] -= 1
    if direction == '^':
        curr_loc[0] -= 1
    if direction == 'v':
        curr_loc[0] += 1
    houses.add((curr_loc[0], curr_loc[1]))
print(len(houses))

# Part 2
houses = set()
houses.add(origin)

santa_curr_loc = [0, 0]
robo_curr_loc = [0, 0]
for i in range(len(directions)):
    if i % 2 == 0:
        if directions[i] == '>':
            santa_curr_loc[1] += 1
        if directions[i] == '<':
            santa_curr_loc[1] -= 1
        if directions[i] == '^':
            santa_curr_loc[0] -= 1
        if directions[i] == 'v':
            santa_curr_loc[0] += 1
        houses.add((santa_curr_loc[0], santa_curr_loc[1]))
    else:
        if directions[i] == '>':
            robo_curr_loc[1] += 1
        if directions[i] == '<':
            robo_curr_loc[1] -= 1
        if directions[i] == '^':
            robo_curr_loc[0] -= 1
        if directions[i] == 'v':
            robo_curr_loc[0] += 1
        houses.add((robo_curr_loc[0], robo_curr_loc[1]))
print(len(houses))