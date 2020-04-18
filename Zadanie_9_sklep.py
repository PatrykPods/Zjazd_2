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
            print(f"{name} w cenie {price} PLN")


        item = input("co chcesz kupic?")

        if item in products :
            counter = input(f"ile chcesz kupic {item}?")
            counter = float(counter)

            if counter <= magazyn[item] :
                print(f"za {counter} kg {item} zaplacisz {counter * products[item]:.2f}")
                magazyn[item] = magazyn[item] - counter
            else:
                print("nie mamy tyle produktów")
    elif komenda == "m":
        komenda_2 = input("co chcesz zrobic? [n-dodaj nowy towar] [i-dodaj do zapasow]")
        if komenda_2 == "n" :
            nazwa = input("podaj nazwe towaru:")
            cena = float(input("podaj cene:"))
            ilosc = int(input("podaj ilosc"))

            magazyn[f"{nazwa}"] = f"{ilosc}"
            products[f"{nazwa}"] = f"{cena}"
        elif komenda_2 == "i" :
            nazwa = input("podaj nazwe")
            ilosc = int(input("podaj ilosc towaru"))

            for nazwa in magazyn :
                magazyn[f"{nazwa}"] = magazyn[f"{nazwa}"] + ilosc
