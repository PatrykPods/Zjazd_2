x = list(range(0,110))
print([el/10 for el in x[0:11:1]])

print([(el, el ** 3, el ** 2) for el in range(-10, 10)])

x = {"asdasd", "dasfas", "asdasd",}

print(dict({el: len(el) for el in x}))