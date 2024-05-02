def evaluate_wire(wire, wires, values):
    if wire in values:
        return values[wire]
    
    if wire.isdigit():
        return int(wire)
    
    operation, input_wires = wires[wire]
    
    if operation == 'AND':
        result = evaluate_wire(input_wires[0], wires, values) & evaluate_wire(input_wires[1], wires, values)
    elif operation == 'OR':
        result = evaluate_wire(input_wires[0], wires, values) | evaluate_wire(input_wires[1], wires, values)
    elif operation == 'LSHIFT':
        result = evaluate_wire(input_wires[0], wires, values) << int(input_wires[1])
    elif operation == 'RSHIFT':
        result = evaluate_wire(input_wires[0], wires, values) >> int(input_wires[1])
    elif operation == 'NOT':
        result = ~evaluate_wire(input_wires[0], wires, values)
    else:
        result = evaluate_wire(input_wires[0], wires, values)
    
    values[wire] = result & 0xFFFF
    return values[wire]

def main():
    wires = {}
    with open('day7input.txt') as file:
        for line in file:
            parts = line.strip().split(' -> ')
            output_wire = parts[1]
            input_parts = parts[0].split()
            
            if len(input_parts) == 1:
                wires[output_wire] = ('ASSIGN', input_parts)
            elif len(input_parts) == 2:
                wires[output_wire] = (input_parts[0], input_parts[1:])
            else:
                wires[output_wire] = (input_parts[1], input_parts[0::2])
    
    values = {}
    wire_a_signal = evaluate_wire('a', wires, values)
    print(f"Signal provided to wire 'a' (first pass): {wire_a_signal}") # Part 1
    
    wires['b'] = ('ASSIGN', [str(wire_a_signal)])
    
    values = {'b': wire_a_signal}
    
    new_wire_a_signal = evaluate_wire('a', wires, values)
    print(f"Signal provided to wire 'a' (second pass): {new_wire_a_signal}") # Part 2

if __name__ == '__main__':
    main()