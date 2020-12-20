from string import ascii_lowercase as alphabet
def read_data():
    '''
    Parses data in to a list of tuples, of the following format:
    ((min_bounds: int, max_bounds:int), letter:str, password:string)
    '''

    with open('2.txt', 'r') as f:
        data = f.read().split('\n')[:-1]
        parsed_data = []

        for entry in data:
            d = entry.split(' ')
            bounds = list(map(lambda k: int(k), d[0].split('-')))
            parsed_data.append((bounds, d[1][:-1], d[2]))
        
        return parsed_data

#print(read_data())
data = read_data()

count = 0
for entry in data:
    min_bound, max_bound = entry[0]
    letter = entry[1]
    password = entry[2]
    # Hash and go through each entry
    res = { a: 0 for a in alphabet }

    # Simplify (given we use alphabet now)
    # Adjust for part 2 (only 1 of 2 positions can contain the letter)

    print(entry[0])
    # Part 2 -- 1 MUST be true for password to be valid
    if (int(password[min_bound-1] == letter) ^ int(password[max_bound-1] == letter)):
        count += 1

    ''' Part 1
    for p in password:
        if p in res:
            res[p] += 1
        else:
            res[p] = 0

    # 0 should be valid; initialize with string alphabet
    if res[letter] >= min_bound and res[letter] <= max_bound:
        count += 1
    else:
        print(entry)
    '''

    #print(res)
    #[ res[ch] in password ]
print(count)
