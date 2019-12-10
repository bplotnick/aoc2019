#!/usr/bin/env python3

def get_fuel(mass):
    fuel = (mass//3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + get_fuel(fuel)

def part1():
    total = 0
    with open('input.txt') as f:
        for i in f:
            total += get_fuel(int(i))
    print(total)

def part2():
    total = 0
    with open('input.txt') as f:
        for i in f:
            total += get_fuel(int(i))
    print(total)    

part2()
