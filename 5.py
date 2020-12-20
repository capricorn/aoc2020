def read_data():
    with open('5.txt', 'r') as f:
        return f.read()

data = read_data().split('\n')[:-1]

#rows = [ 'FBFBBFFRLR' ]
#rows = [ line[:7] for line in data ]
rows = data
passes = []
seat = []
for row in rows:
    min_row = 0
    max_row = 127

    for letter in row[:6]:
        print(letter)
        min_row, max_row = {
            'F': (min_row, min_row+(max_row - min_row)//2), 
            'B': (min_row+(max_row - min_row)//2+1, max_row),
        }[letter]
        print(min_row, max_row)

    the_row = {'F': min(min_row,max_row), 'B': max(min_row,max_row)}[row[6]]

    min_col = 0
    max_col = 7
    for letter in row[7:-1]:
        min_col, max_col = {
            'L': (min_col, min_col+(max_col - min_col)//2),
            'R': (min_col+(max_col - min_col)//2+1, max_col),
        }[letter]

    the_col = {'L': min(min_col,max_col), 'R': max(min_col,max_col)}[row[-1]]

    passes.append(the_row * 8 + the_col)
    seat.append((the_row, the_col))
    #print(min_row, max_row)

# Sloppy
print(max(passes))
print([(p1,p2) for p1, p2 in zip(sorted(passes), sorted(passes)[1:]) if p2 - p1 == 2])

'''
print(set(range(0, 128)) - set([row for row, _ in seat]))
print(set(range(0, 8)) - set([col for _, col in seat]))

print(set([col for _, col in seat]))
print(set([row for row, _ in seat]))
'''
# 0-127 rows, 0-7 columns. All should exist
