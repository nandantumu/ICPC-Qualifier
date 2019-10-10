import sys

numbers = list()

for line in sys.stdin:
    numbers.append(int(line.strip()))
numbers = numbers[1:]

missed = list(range(1, numbers[-1]+1, 1))

for i in numbers:
    if i in missed:
        missed.remove(i)

if missed:
    for i in missed:
        print(i)
else:
    print('good job')