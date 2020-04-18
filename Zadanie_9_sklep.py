prices = {
    "ziemniaki" : 1.99,
    "pomidory" : 1.50,
    "piwo" : 2.50,
    "jabłka" : 1.20,
}

item = input("co chcesz kupic?")

print(prices.get(f"{item}", "brak produktu"))