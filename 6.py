from functools import reduce

def read_data():
    with open('6.txt', 'r') as f:
        return f.read()

data = read_data().split('\n\n')
'''
In each group, set such that everyone answered yes (intersection)
'''
#data = [ len(set(d.replace('\n', ''))) for d in data ]

data = [ d.strip().split('\n') for d in data ]
print(data)
data = [ [ set(b) for b in a ] for a in data ]
data = [ len(reduce(lambda x,y: x & y, s)) for s in data ]
print(sum(data))
#print(sum(data))

