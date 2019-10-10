import sys

P,D = map(int, sys.stdin.readline().split())

precints = list() # List of tuples (District, VotesA, VotesB)

for line in sys.stdin:
    district, votesa, votesb = map(int,line.split())
    precints.append(tuple((district, votesa, votesb)))

class District:
    def __init__(self, name):
        self.name = name
        self.votesa = 0
        self.votesb = 0
        self.wastea = 0
        self.wasteb = 0
        self.effgap = 0
        self.winner = None

    @property
    def totalvotes(self):
        return self.votesb + self.votesa
    
    @property
    def majthresh(self):
        return (self.totalvotes//2)+1


districts = [District(i+1) for i in range(D)]

for precint in precints:
    distid = precint[0]
    votesa = precint[1]
    votesb = precint[2]
    districts[distid-1].votesa += votesa
    districts[distid-1].votesb += votesb

totalwastea = 0
totalwasteb = 0
totalvotes = 0

for dist in districts:
    # Define the winner. Note: there are no ties.
    if dist.votesa > dist.votesb:
        dist.winner = 'A'
    else:
        dist.winner = 'B'
    
    # Let's define wasted votes
    if dist.winner == 'A':
        dist.wasteb = dist.votesb
        dist.wastea = dist.votesa-dist.majthresh
    else: # B won
        dist.wastea = dist.votesa
        dist.wasteb = dist.votesb-dist.majthresh

    # Let's define eff gap

    dist.effgap = abs(dist.wastea-dist.wasteb)/dist.totalvotes

    print("{} {} {}".format(dist.winner, dist.wastea, dist.wasteb))
    totalwastea += dist.wastea
    totalwasteb += dist.wasteb
    totalvotes += dist.totalvotes

effgap = abs(totalwastea-totalwasteb)/totalvotes
print(effgap)