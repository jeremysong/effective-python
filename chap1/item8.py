import itertools

names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

names.append('Rosalind')

for name, count in itertools.zip_longest(names, counts, fillvalue=0):
    print(f'{name}: {count}')