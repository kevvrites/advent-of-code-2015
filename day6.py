file = open('day6input.txt', 'r')
directions = file.readlines()

grid = [[0 for element in range(1000)] for y in range(1000)]

# Part 1
# def toggle(x1, y1, x2, y2):
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             if grid[i][j] == 0:
#                 grid[i][j] = 1
#             else:
#                 grid[i][j] = 0

# def turnOn(x1, y1, x2, y2):
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             grid[i][j] = 1

# def turnOff(x1, y1, x2, y2):
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             grid[i][j] = 0
    
# for direction in directions:
#     direction = direction.split(' ')
#     if direction[0] == "turn":
#         coor1 = direction[2].split(',')
#         coor2 = direction[4].split(',')
#         print(coor1[0], coor1[1], coor2[0], coor2[1])
#         if direction[1] == "on":
#             turnOn(int(coor1[0]), int(coor1[1]), int(coor2[0]), int(coor2[1]))
#         if direction[1] == "off":
#             turnOff(int(coor1[0]), int(coor1[1]), int(coor2[0]), int(coor2[1]))
#     else:
#         coor1 = direction[1].split(',')
#         coor2 = direction[3].split(',')
#         print(coor1[0], coor1[1], coor2[0], coor2[1])
#         toggle(int(coor1[0]), int(coor1[1]), int(coor2[0]), int(coor2[1]))


# count = 0
# for i in range(1000):
#     for j in range(1000):
#         if grid[i][j] == 1:
#             count += 1
# print(count)

# Part 2
def toggle(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] += 2

def turnOn(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] += 1

def turnOff(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] -= 1
            if grid[i][j] < 0:
                grid[i][j] = 0
    
for direction in directions:
    direction = direction.split(' ')
    if direction[0] == "turn":
        coor1 = direction[2].split(',')
        coor2 = direction[4].split(',')
        if direction[1] == "on":
            turnOn(int(coor1[0]), int(coor1[1]), int(coor2[0]), int(coor2[1]))
        if direction[1] == "off":
            turnOff(int(coor1[0]), int(coor1[1]), int(coor2[0]), int(coor2[1]))
    else:
        coor1 = direction[1].split(',')
        coor2 = direction[3].split(',')
        toggle(int(coor1[0]), int(coor1[1]), int(coor2[0]), int(coor2[1]))

count = 0
for i in range(1000):
    for j in range(1000):
        count += grid[i][j]
print(count)