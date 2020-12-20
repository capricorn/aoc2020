from sys import exit
from math import prod
from itertools import combinations as c

'''
Goal:
    find the two entries that sum to 2020
    slow solution is to generate all pairs (combinations),
    (n choose 2), and then find the pair that sums 
'''

def read_data():
    # Should've converted data to int
    with open('1.txt', 'r') as f:
        return f.read().split()

#print(read_data())
# Some number theory would produce a much better result


def part1(data):
    print(len(data))
    pairs = list(c(data, 2))

    res = list(filter(lambda p: int(p[0]) + int(p[1]) == 2020, pairs))[0]
    print(res)
    print(int(res[0]) * int(res[1]))


# Works, doesn't scale; need better filter
def part2(data):
    print(len(data))
    data = list(map(lambda d: int(d), data))
    trips = list(c(data, 3))
    res = list(filter(lambda p: sum(p) == 2020, trips))[0]
    print(res)
    #print(int(res[0]) * int(res[1]))
    print(prod(res))


data = read_data()
part2(data)
