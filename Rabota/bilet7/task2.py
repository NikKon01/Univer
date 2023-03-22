def scramble(str1: str(input()), str2: str(input())):
        d = {}
        for i in str1:
            if not i in str2:
                d[i] = 0
            d[i] += 1
        for i in str2:
            if not i in d or d[i] < 1:
                return False
            d[i] -= 1
        return True
print(scramble())

