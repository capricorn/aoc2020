from re import fullmatch as match
from math import prod

def read():
    with open('4.txt', 'r') as f:
        return [ entry.replace('\n', ' ').split() for entry in f.read().split('\n\n') ]

#print(read())
tags = {
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
}

# Unfortunately need to be more thorough, just write
# regex for grammar validation, followed by and
valid = {
    'byr': lambda v: (match('\d{4}', v) != None) and (1920 <= int(v) <= 2002),
    'iyr': lambda v: (match('\d{4}', v) != None) and (2010 <= int(v) <= 2020),
    'eyr': lambda v: (match('\d{4}', v) != None) and (2020 <= int(v) <= 2030),
    'hgt': lambda v: (match('\d+(cm|in)', v) != None) and ((150 <= int(v[:-2]) <= 193) if v[-2:] == 'cm' else (59 <= int(v[:-2]) <= 76)),
    'hcl': lambda v: (match('#[a-f0-9]{6}', v) != None),
    'ecl': lambda v: v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda v: match('[0-9]{9}', v) != None,
}

count = 0
for entry in read():
    # Now need to extract actual data
    pairs = [ tag.split(':') for tag in entry ]
    print(pairs)

    #continue
    # How many tags match
    ''' p1
    if sum([ int(tag[:3] in tags) for tag in entry ]) == len(tags):
        count += 1
    '''
    tag_cnt = sum([ int(tag[:3] in tags) for tag in entry ])
    all_valid = prod([ int(valid[tag](val)) for tag, val in pairs if tag in valid ])

    if (tag_cnt == len(tags)) and all_valid == 1:
        count += 1

print(count)
