from hashlib import md5

code = "iwrupvqb"

# Part 1
for i in range(1000000):
    decimal = md5((code + str(i)).encode()).hexdigest()
    if decimal[:5] == '00000':
        print(i)
        break

# Part 2
for i in range(1000000000):
    decimal = md5((code + str(i)).encode()).hexdigest()
    if decimal[:6] == '000000':
        print(i)
        break