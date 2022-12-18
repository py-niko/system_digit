x = input()
degree = len(x)-1
digit = 0

while degree > -1:
    for j in x:
        k = int(j) * 2**degree
        digit += k
        degree -= 1

print(digit)

