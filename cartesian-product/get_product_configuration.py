import itertools

sizes = {'S', 'M', 'L'}
colors = {'red', 'blue', 'green'}

configurations = list(itertools.product(sizes, colors))
print(configurations)
