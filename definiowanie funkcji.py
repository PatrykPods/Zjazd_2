def przywitanie() :
    print("hello world!")
    return "hello world!"

przywitanie()

x = przywitanie()

print(3, x)

def przywitanie(name) :
    text = f"hello {name}"
    print(text)
    return text

przywitanie("Patryk")

def incrementation(poczatek, krok = 1) :
    return poczatek + krok

print(incrementation(10, 3)) #13
print(incrementation(10)) #11





def zlacz_teksty(lista_tekstow):
    return " ".join(lista_tekstow)

def zlacz_teksty(*args, **kwargs) :
    print(args)
    print(kwargs)
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(k, str(v))
    return text


kolekcja = [(10, "Z"), (5, "c"), (15, "a")]

print(sorted(kolekcja))

def second(x):
    return x[1]

print(sorted(kolekcja, key = second))

print(sorted(kolekcja, key = lambda x: x[1]))

def decrement(n):
    if n == 0:
        print(0)
        return
    print(n)
    decrement(n-1)

decrement(10)