import sys

schedule = [char for char in sys.stdin.readline().strip()]

from itertools import chain, combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class MultiSet():
    def __init__(self):
        self.dict = dict()
    
    def add(self, item):
        if item in self.dict:
            self.dict[item] += 1
        else:
            self.dict[item] = 1
    
    def get(self, item):
        if item in self.dict:
            return self.dict[item]
        else:
            return 0

    @property
    def items(self):
        return list(self.dict.keys())

schedule_set = MultiSet()

for elem in schedule:
    schedule_set.add(elem)

key_combs = powerset(schedule_set.items)
total_scheds = 0

for comb in key_combs:
    if len(comb)<2:
        continue
    else:
        scheds = 1
        for item in comb:
            scheds *= schedule_set.get(item)
        total_scheds += scheds

print(total_scheds)