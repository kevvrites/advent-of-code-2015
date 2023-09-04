file = open('day5input.txt', 'r')
strings = file.readlines()

# Part 1
def checkVowelCount(string):
    count = 0
    for letter in string:
        if letter in 'aeiou':
            count += 1
    if count >= 3:
        return False
    return True

def checkRepeating(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
    return False

def niceString(string):
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        return False
    if checkVowelCount(string):
        return False
    return checkRepeating(string)

count = 0
for string in strings:
    if niceString(string):
        count += 1
print(count)

# Part 2
def checkRepeatingPair(string):
    pairs = set()
    for i in range(len(string) - 1):
        if string[i:i+2] in pairs:
            if string[i:i+2] != string[i-1:i+1]:
                return True
        else:
            pairs.add(string[i:i+2])
    return False

def checkRepeatingWithBetween(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2] :
            return True
    return False

count = 0
for string in strings:
    if checkRepeatingPair(string):
        if checkRepeatingWithBetween(string):
            count += 1
print(count)