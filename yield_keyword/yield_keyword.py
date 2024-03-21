def fetch_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

zen = fetch_lines('zenofpython.txt')
print(next(zen))
print(next(zen))
print(next(zen))
print(next(zen))
print(next(zen))