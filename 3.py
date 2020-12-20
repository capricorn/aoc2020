import numpy as np
from math import prod

def read_map():
    with open('3.txt', 'r') as f:
        data = f.read()
        # Would be nice if numpy could automatically generate the table
        # for us.. maybe pandas can..?
        width = data.index('\n')
        data = data.replace('\n', '')
        print(data)
        height = len(data) // width

        data = np.char.array(list(data), itemsize=1)
        data = data.reshape((height,width))

        return data

trees = read_map()
rows, cols = trees.shape
print(rows,cols)

'''
Could be cleaner
'''
def traverse(x_step, y_step):
    f = lambda x: (-y_step/x_step)*x

    x = 0
    cnt = 0
    while (y := int(abs(f(x)))) < rows:
        cnt += 1 if trees[y][x % cols] == '#' else 0
        x += x_step

    print(cnt)
    return cnt

print(prod(map(lambda f: traverse(*f), [(1,1),(3,1),(5,1),(7,1),(1,2)])))
