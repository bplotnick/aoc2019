#!/usr/bin/env python3
import numpy as np
import sys

def _find_extents(x, extents):
    max_x, min_x, max_y, min_y = extents
    cur_x = cur_y = 0
    for i in x:
        if i[0] == 'R':
            cur_x += int(i[1:])
            max_x = max(max_x, cur_x)
        elif i[0] == 'L':
            cur_x -= int(i[1:])
            min_x = min(min_x, cur_x)
        elif i[0] == 'D':
            cur_y += int(i[1:])
            max_y = max(max_y, cur_y)
        elif i[0] == 'U':
            cur_y -= int(i[1:])
            min_y = min(min_y, cur_y)
    return (max_x, min_x, max_y, min_y)
    
def find_extents(in1, in2):
    extents = (0,0,0,0)
    extents = _find_extents(in1, extents)
    extents = _find_extents(in2, extents)
    return extents

def fill_board(board, delays, in1, start):
    steps = -1
    start_x, start_y = cur_x, cur_y = start
    for i in in1:
        seg_x = cur_x
        seg_y = cur_y
        if i[0] == 'R':
            for j in range(cur_x, cur_x+int(i[1:])+1):
                c = (j, cur_y)
                board[c] = True
                steps += 1
                delays[c] = min(delays[c], steps)
            cur_x += int(i[1:])
        elif i[0] == 'L':
            for j in range(cur_x, cur_x-int(i[1:])-1, -1):
                c = (j, cur_y)
                board[c] = True
                steps += 1
                delays[c] = min(delays[c], steps)
            cur_x -= int(i[1:])
        elif i[0] == 'D':
            for j in range(cur_y, cur_y+int(i[1:])+1):
                c = (cur_x, j)
                board[c] = True
                steps += 1
                delays[c] = min(delays[c], steps)
            cur_y += int(i[1:])
        elif i[0] == 'U':
            for j in range(cur_y, cur_y-int(i[1:])-1, -1):
                c = (cur_x, j)
                board[c] = True
                steps += 1
                delays[c] = min(delays[c], steps)
            cur_y -= int(i[1:])
        steps -=1
    board[start_x, start_y] = False
    delays[start_x, start_y] = np.inf
    return board, delays


def part1():
    with open("input.txt") as f:
        i = f.readlines()
        in1 = [x for x in i[0].split(',')]
        in2 = [x for x in i[1].split(',')]
    e = find_extents(in1, in2)
    board1 = np.full((e[0]-e[1]+1,e[2]-e[3]+1), False)
    board2 = np.full((e[0]-e[1]+1,e[2]-e[3]+1), False)
    delays1 = np.full((e[0]-e[1]+1,e[2]-e[3]+1), np.inf)
    delays2 = np.full((e[0]-e[1]+1,e[2]-e[3]+1), np.inf)
    start = (-e[1], -e[3])
    board1, delays1 = fill_board(board1, delays1, in1, start)
    board2, delays2 = fill_board(board2, delays2, in2, start)
    r = np.logical_and(board1, board2)
    results = np.argwhere(r == True)
    mins = [delays1[x,y] + delays2[x,y] for x,y in results]
    print(min(mins))

part1()
