zbior = set()
zbior_1 = set()

while True :

    liczba = input("podaj liczbe od 0 do 100 jesli chcesz skonczyc wpisz 'x':")

    if liczba == "x" :
        break
    else :
        liczba = float(liczba)
        zbior.add(liczba)

    if liczba % 2 == 0 :
        zbior_1.add(liczba)

print(f"liczba liczb: {len(zbior)}")
print(f"liczba liczb parzystych: {len(zbior_1 & zbior)}")