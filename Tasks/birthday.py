
import random

for p in range(2, 23):
    st = 0
    for k in range(1, 10000):
        birthday = []
        for i in range(0, p):
            bday = random.randrange(0, 365)
            birthday.append(bday)
        set_of_bdays = set(birthday)
        if len(set_of_bdays) < len(birthday):
            st += 1
rez = st/10000
print(rez)

