import random

birthday = []
st = 0

for i in range(1, 100000):
    dr = [random.randint(1, 365) for i in range(23)]
    if len(dr) != len(set(dr)):
       st += 1
