import random

# seq = range(100)
# random.shuffle(seq)

seq = [1, 2, 1, 0, 6, 3]

flag = True
number = 0

i = 1
while (i < len(seq) - 1 and number <= 2):
    if seq[i] > seq[i - 1] and seq[i] > seq[i + 1] and seq[i] % 2 == 0:
        number += 1
    i += 1

print(number == 2)