import re

def encode(line):
    encoded_line = '"'
    for char in line:
        if char == '"':
            encoded_line += '\\"'
        elif char == '\\':
            encoded_line += '\\\\'
        else:
            encoded_line += char
    encoded_line += '"'
    return encoded_line

def main():
    sum_str_chars = 0
    sum_mem_chars = 0

    sum_encoded_chars = 0
    sum_code_chars = 0

    with open('day8input.txt') as file:
        for line in file:
            str_lit = line.strip()
            str_mem = eval(str_lit)
            
            sum_str_chars += len(str_lit)
            sum_mem_chars += len(str_mem)

            encoded_str = encode(str_lit)
            sum_encoded_chars += len(encoded_str)
            sum_code_chars += len(str_lit)
            
    print(sum_str_chars - sum_mem_chars) # Part 1
    print(sum_encoded_chars - sum_code_chars) # Part 2

if __name__ == '__main__':
    main()