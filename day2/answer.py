#!/usr/bin/env python3

def calc(vals):
    idx = 0

    while True:
        operator = vals[idx]
        if operator == 99:
            return vals
        elif operator == 1:
            op1 = vals[idx+1]
            op2 = vals[idx+2]
            out = vals[idx+3]
            vals[out] = vals[op1] + vals[op2]
        elif operator == 2:
            op1 = vals[idx+1]
            op2 = vals[idx+2]
            out = vals[idx+3]
            vals[out] = vals[op1] * vals[op2]
        idx = idx + 4

def program(noun, verb):
    with open('input.txt') as f:
        vals = [int(x) for x in f.read().split(',')]
        vals[1] = noun
        vals[2] = verb
    return calc(vals)

def part1():
    print(program(12, 2))

def part2():
    for noun in range(100):
        for verb in range(100):
            if program(noun,verb)[0] == 19690720:
                print(noun, verb)
#v = part1()
#print(','.join([str(x) for x in v]))
part2()

#print(calc([1,9,10,3,2,3,11,0,99,30,40,50]))
# print(calc([1,0,0,0,99]))
# print(calc([2,3,0,3,99]))
# print(calc([2,4,4,5,99,0]))
# print(calc([1,1,1,4,99,5,6,0,99]))
