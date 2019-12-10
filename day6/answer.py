#!/usr/bin/env python3

class Node:
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name

nodes = {}
depths = {}
def depth(node):
    if node in depths:
        return depths[node]
    if nodes[node].parent == None:
        assert nodes[node].name == 'COM'
        return 0
    d = depth(nodes[node].parent) + 1
    depths[node] = d
    return d

def orb_xfer(node1, node2):
    # distance between two nodes
    dist = 0
    curnode1 = node1
    curnode2 = node2
    while curnode1 != curnode2:
        if depth(curnode1.name) > depth(curnode2.name):
            curnode1 = nodes[curnode1.parent]
        else:
            curnode2 = nodes[curnode2.parent]
        dist += 1
    return dist

def answer():
    with open('input.txt') as f:
        x = f.readlines()
    for line in x:
        left, right = line.split(')')
        right = right.rstrip()
        if left not in nodes:
            nodes[left] = Node(left)
        nodes[right] = Node(right)
        nodes[right].parent = left
        nodes[left].children.append(nodes[right])

    # part 1
    orbs = 0
    for node in nodes:
        orbs += depth(node)
    print(orbs)

    # part 2
    xfer = orb_xfer(nodes[nodes['YOU'].parent], nodes[nodes['SAN'].parent])
    print(xfer)
    
answer()
