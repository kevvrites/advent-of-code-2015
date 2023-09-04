file = open('day2input.txt', 'r')
sizes = file.readlines()

# Part 1
sqft = 0
for item in sizes:
    item = [int(i) for i in item.strip().split('x')]
    l = max(item)
    h = min(item)
    item.remove(l)
    item.remove(h)
    w = item[0]
    sa = 2*l*w + 3*w*h + 2*h*l
    sqft += sa
print(sqft)

# Part 2
length = 0
for item in sizes:
    item = [int(i) for i in item.strip().split('x')]
    l = max(item)
    h = min(item)
    item.remove(l)
    item.remove(h)
    w = item[0]
    bow = w+w+h+h + l*w*h
    length += bow
print(length)