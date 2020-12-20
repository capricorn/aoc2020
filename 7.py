from re import fullmatch
import itertools
import sys

import cc

def read():
    with open('7.txt', 'r') as f:
        return f.read()

data = read().split('\n')[:-1]

# Need to recursively follow bags to see if it can contain a gold bag
bag_types = [ ''.join(d.split()[0:2]) for d in data ]

# Find all indices that contain a number, extract next two from those to get mapping
# Indices to produce mapping
# Ignores bags that contain nothing
idxs = [ [ ''.join(d.split()[i+1:i+3]) for i, word in enumerate(d.split()) if fullmatch('\d+', word) != None ] for d in data ]

mapping = ({ bag: set(items) for bag, items in zip(bag_types, idxs) })

# Connected components of all bags; lets us find bags that can eventually find shiny gold
g = cc.cc(mapping)
holders = { key for key in g if g[key] & {'shinygold'} != set() }
# Part 1
print(len(holders))

bag_count = { bag: { ''.join(d.split()[i+1:i+3]): int(word) for i, word in enumerate(d.split()) if fullmatch('\d+', word) != None } for bag, d in zip(bag_types, data) }

# calculate total number of bags contained by a single bag (recursive)
def bag_total(bag, count):
    '''
    bag = { bag_type: cnt, ... }
    count = { bag_type: bag, ... }

    return sum([ cnt*bag_total(btype) for btype, cnt in bag.items() ])
    '''

    # Number of bags in this bag multiplied by their contents
    return sum([ cnt + cnt*bag_total(count[btype], count) for btype, cnt in bag.items() ])


# Part 2
print(bag_total(bag_count['shinygold'], bag_count))
