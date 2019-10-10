import sys
from string import ascii_uppercase

V = int(sys.stdin.readline())
alpha_vars = [ascii_uppercase[i] for i in range(V)]
truth_vals = list(sys.stdin.readline().split())
circuit = list(sys.stdin.readline().split())

for char in range(len(circuit)):
    if circuit[char] not in ['*', '+', '-']:
        circuit[char] = truth_vals[alpha_vars.index(circuit[char])]

# Now all things are subbed
ops = list()

while circuit:
    ops.append(circuit.pop(0))
    if ops[-1] in ['*', '+', '-']:
        # Because of the way this lang is structured, we can read left to right
        # get the operator
        operator = ops.pop()
        if operator == '*':
            op2 = ops.pop()
            op1 = ops.pop()
            if op1=='T' and op2=='T':
                ops.append('T')
            else:
                ops.append('F')
        if operator == '+':
            op2 = ops.pop()
            op1 = ops.pop()
            if op1=='F' and op2=='F':
                ops.append('F')
            else:
                ops.append('T')
        if operator == '-':
            op1 = ops.pop()
            if op1=='F':
                ops.append('T')
            else:
                ops.append('F')

print(ops[0])