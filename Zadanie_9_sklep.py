

products = {
    "ziemniaki" : 1.99,
    "pomidory" : 1.50,
    "piwo" : 2.50,
    "jablka" : 1.20,
}

magazyn = {
    "ziemniaki": 10,
    "pomidory": 10,
    "piwo": 10,
    "jablka": 10,
}

while True :

    komenda = input("Co chcesz zrobic? [k-kup] [z-zakoncz] [m-magazyn]")

    if komenda == "z" :
        break
    elif komenda == "k" :

        print("nasz sklep oferuje:")

        for name, price in products.items() :
            print(f"{name} w cenie {price} PLN (stan: {magazyn[name]}")


        item = input("co chcesz kupic?")

        if item in products :
            counter = input(f"ile chcesz kupic [{item}]?")
            counter = float(counter)

            if counter <= magazyn[item] :
                print(f"za {counter} kg {item} zaplacisz {counter * products[item]:.2f}")
                magazyn[item] = magazyn[item] - counter
            else:
                print("nie mamy tyle produktów")
    elif komenda == "m":
        nazwa=input("Co dodajemy?")
        ilosc=int(input(f"podaj ilosc {nazwa}"))
        magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc
        if nazwa not in products:
            cena = float(input(f"podaj cene za {nazwa}"))
            products[nazwa] = cena
    else:
        print("niezrozumiala komenda")