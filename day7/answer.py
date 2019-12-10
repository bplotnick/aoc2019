#!/usr/bin/env python3
import asyncio
import operator
import itertools

async def calc(vals, valq, resultq):
    rval = 0
    idx = 0

    while True:
        inst = str(vals[idx]).zfill(5)
        opcode = int(inst[-2:])
        modes = inst[:-2]
        if opcode == 99:
            return rval
        elif opcode == 1:
            op1 = vals[idx+1]
            val1 = vals[op1] if modes[-1] == '0' else op1
            op2 = vals[idx+2]
            val2 = vals[op2] if modes[-2] == '0' else op2
            out = vals[idx+3]
            vals[out] = val1 + val2
            idx = idx + 4
        elif opcode == 2:
            op1 = vals[idx+1]
            val1 = vals[op1] if modes[-1] == '0' else op1
            op2 = vals[idx+2]
            val2 = vals[op2] if modes[-2] == '0' else op2
            out = vals[idx+3]
            vals[out] = val1 * val2
            idx = idx + 4
        elif opcode == 3:
            out = vals[idx+1]
            vals[out] = await valq.get()
            valq.task_done()
            idx = idx + 2
        elif opcode == 4:
            out = vals[idx+1]
            rval = vals[out] if modes[-1] == '0' else out
            idx = idx + 2
            resultq.put_nowait(rval)
        elif opcode == 5 or opcode == 6:
            op1 = vals[idx+1]
            val1 = vals[op1] if modes[-1] == '0' else op1
            op2 = vals[idx+2]
            val2 = vals[op2] if modes[-2] == '0' else op2
            if (val1 != 0) ^ (opcode == 6):
                idx = val2
            else:
                idx = idx + 3
        elif opcode == 7 or opcode == 8:
            opmap = {
                7: operator.lt,
                8: operator.eq,
            }
            op1 = vals[idx+1]
            val1 = vals[op1] if modes[-1] == '0' else op1
            op2 = vals[idx+2]
            val2 = vals[op2] if modes[-2] == '0' else op2
            out = vals[idx+3]
            if opmap[opcode](val1, val2):
                vals[out] = 1
            else:
                vals[out] = 0
            idx = idx + 4

async def program(stages):
    queues = []
    for i in stages:
        q = asyncio.Queue()
        queues.append(q)
        q.put_nowait(i)

    progs = []
    for i in range(len(stages)):
        with open('input.txt') as f:
            progs.append(calc([int(x) for x in f.read().split(',')], queues[i], queues[(i+1)%len(stages)]))

    queues[0].put_nowait(0)
    return (await asyncio.gather(*progs))[-1]

def ans():
    coros = []
    for p in itertools.permutations(range(5,10)):
        coros.append(program(p))
    import ipdb
    ipdb.set_trace()
    loop = asyncio.get_event_loop()

    vals = loop.run_until_complete(asyncio.gather(*coros))
    return max(vals)

print(ans())
#print(','.join([str(x) for x in v]))
#part2()

#print(calc([1,9,10,3,2,3,11,0,99,30,40,50]))
# print(calc([1,0,0,0,99]))
# print(calc([2,3,0,3,99]))
# print(calc([2,4,4,5,99,0]))
# print(calc([1,1,1,4,99,5,6,0,99]))
