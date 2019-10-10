import sys

submitted = int(sys.stdin.readline())
papers = list(map(int,sys.stdin.readline().split()))

from itertools import chain, combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def get_exval(submitted, papers):
    all_combs = powerset(range(submitted))
    e_val = 0
    for comb in all_combs:
        # Calc prob of occurring, and value
        setcomb = set(comb)
        probs = list()
        for i in range(len(papers)):
            if i in setcomb:
                probs.append(papers[i]/100)
            else:
                probs.append((100-papers[i])/100)
        prob = 1
        for p in probs:
            prob *= p
        
        if len(comb) == 0:
            value = 0
        else:
            value = (len(comb))**(len(comb)/submitted)
        e_val += (prob*value)
    return e_val


all_combs = powerset(range(submitted))
# What are the possible papers she could submit?
max_exval = 0
for comb in all_combs:
    submitted = len(comb)
    comb = set(comb)
    paps = [papers[i] for i in comb]
    exval = get_exval(submitted, paps)
    if exval > max_exval:
        max_exval = exval

print(max_exval)