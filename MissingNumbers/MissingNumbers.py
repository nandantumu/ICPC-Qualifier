import sys

numbers = list()

for line in sys.stdin:
    numbers.append(int(line.strip()))

end = numbers[-1]
missed = list()
lastnum=end
hitone = False

for i in reversed(numbers[:-1]):
    if not i == lastnum-1:
        # something was missed.
        distance = lastnum - i - 1
        for j in range(1,distance+1):
            missed.append(lastnum-j)
    else:
        # nothing was missed
        pass
    if lastnum == 1:
        hitone = True
    lastnum = i

if not hitone:
    missed.append(1)

if len(missed)==0:
    print('good job')
else:
    for i in reversed(missed):
        print(i)