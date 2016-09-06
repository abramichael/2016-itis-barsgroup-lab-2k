import random

maximum = reduce(lambda x, y: x if x > y else y, [random.randrange(100) for i in range(20)])

# read about map, reduce, filter, zip

print maximum

