x = list(range(1,11))

print(x)

szesciany = []

for el in x :
    if el % 2 == 0 :
        szesciany.append(el ** 3)

print(szesciany)

print([el ** 3 for el in x if el % 2 == 0])